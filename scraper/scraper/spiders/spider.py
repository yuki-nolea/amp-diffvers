import scrapy
import csv
import re
import boto3
from botocore.exceptions import ClientError

# Zabbixウェブサイトからパラメータ一覧を取得し、AWS DynamoDB に取得したパラメータを格納するスパイダー
class ZabbixParamsSpider(scrapy.Spider):

  # scrapyコマンドによる実行対象spider指定用の名前
  name = "spider"

  # dynamodb インスタンス
  dynamodb = boto3.resource('dynamodb') 

  # Zabbixウェブサイト
  def start_requests(self):
    # Zabbixウェブサイトから取得したいパラメータ一覧のバージョン、プロセスを指定
    list1=["4.0", "5.0", "6.0", "4.0", "5.0", "6.0"]
    list2=["Zabbix server", "Zabbix server", "Zabbix server", "Zabbix agent (UNIX)", "Zabbix agent (UNIX)", "Zabbix agent (UNIX)"]
    list3=["zabbix_server", "zabbix_server", "zabbix_server", "zabbix_agentd", "zabbix_agentd", "zabbix_agentd"]
    list4=["ZabbixServer", "ZabbixServer", "ZabbixServer", "ZabbixAgent_UNIX", "ZabbixAgent_UNIX", "ZabbixAgent_UNIX"]

    # スクレイピングを実行するリクエストを実行
    for i in range(len(list1)):
      response = scrapy.Request("https://www.zabbix.com/documentation/"+list1[i]+"/en/manual/appendix/config/"+list3[i], self.parse)
      response.meta["version"] = list1[i]
      response.meta["process"] = list2[i]
      response.meta["process_alias"] = list4[i]
      yield response

  # スクレイピングにより取得したデータをDynamoDBへ格納する
  def parse(self, response):
    version = response.meta["version"]
    process = response.meta["process"]
    process_alias = response.meta["process_alias"]
    
    # パラメータが記載されている表データを取得
    div_tables = response.css('div.table-container')

    # 表のセルを抽出しリスト変換
    table = div_tables.css('td').getall()

    # htmlタグを削除し、テキストデータを抽出
    rtable = []
    for sb in table:
      # aタグを削除
      s = (re.sub("<a.*?>", "",sb).replace('</a>', ''))
      
      # 2列結合セルの場合
      if '<td colspan="2">' in s:
        text = (s.replace('<td colspan="2">', '').replace('</td>', '')) # tdタグを削除
        rtable.append(text) # テキストデータを追加
        rtable.append('') # 2列目のデータは空として追加
      
      # 3列結合セルの場合
      elif '<td colspan="3">' in s:
        text = (s.replace('<td colspan="3">', '').replace('</td>', '')) # tdタグを削除
        rtable.append(text) # テキストデータを追加
        rtable.append('') # 2列目のデータは空として追加
        rtable.append('') # 3列目のデータは空として追加

      # 非結合セルの場合
      elif '<td>' in s:
        text = (s.replace('<td>', '').replace('</td>', '')) # tdタグを削除
        rtable.append(text) # テキストデータを追加

      else:
        rtable.append(s)
    
    # 表データの行（5列）ごとに配列データを分割
    def split_list(rtable, n):
      for idx in range(0, len(rtable), n):
        yield rtable[idx:idx + n]
    
    ntable = list(split_list(rtable, 5))
    
    # DB投入用に各行データにprocess, version情報を追加
    db = []
    for i in range(len(ntable)):
      db.append(tuple([process, version, ntable[i][1:5]]))

    # csvファイルに行データを保存する
    filename = "zabbix-parameters/" + process_alias + "_" + version + '.csv'
    with open(filename, 'w') as f:
      writer = csv.writer(f)
      writer.writerows(db)

    # dynamodb上に指定のプロセス、バージョンを名前に持つテーブルを作成（存在しない場合のみ作成）
    dynamodb_table = self.create_table(process_alias + "_" + version)

    # 行データをdynamodbに保存
    for i in range(len(db)):
      dynamodb_table.put_item(Item={"Process": db[i][0], "Ver": db[i][1], "ParamName": db[i][2], "Mandatory": db[i][3], "ValRange": db[i][4], "ValDefault": db[i][5], "ParamDesc": db[i][6]})

        
  # DynamoDB上に指定された名前（<tablename>）のテーブルを作成し、参照を返す（<tablename>名のテーブルが存在しない場合のみ）
  def create_table(self, tablename):
    try:
      params = {
        "TableName": tablename,
        "KeySchema": [ {"AttributeName": "ParamName", "KeyType": "HASH"}, ],
        "AttributeDefinitions": [ {"AttributeName": "ParamName", "AttributeType": "S"}, ],
        "ProvisionedThroughput": {"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
      }
      table = self.dynamodb.create_table(**params)

      print(f"Creating {tablename}...")
      table.wait_until_exists()
      return table

    # 指定された名前のテーブルが既に存在している場合はその参照を返す
    except ClientError as e:
      return self.dynamodb.Table(tablename)
    