import scrapy
import csv
import re
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class ScrapyZabbixParamsSpider(scrapy.Spider):
  name = "spider"
  #allowed_domains = ["zabbix.com"]
  dynamodb = boto3.resource('dynamodb')

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

    except ClientError as e:
      # print(e.response)
      # quit()
      return self.dynamodb.Table(tablename)

  def start_requests(self):
    list1=["4.0", "5.0", "6.0", "4.0", "5.0", "6.0"]
    list2=["Zabbix server", "Zabbix server", "Zabbix server", "Zabbix agent (UNIX)", "Zabbix agent (UNIX)", "Zabbix agent (UNIX)"]
    list3=["zabbix_server", "zabbix_server", "zabbix_server", "zabbix_agentd", "zabbix_agentd", "zabbix_agentd"]
    list4=["ZabbixServer", "ZabbixServer", "ZabbixServer", "ZabbixAgent_UNIX", "ZabbixAgent_UNIX", "ZabbixAgent_UNIX"]
    for i in range(len(list1)):
      request = scrapy.Request("https://www.zabbix.com/documentation/"+list1[i]+"/en/manual/appendix/config/"+list3[i], self.parse)
      request.meta["version"] = list1[i]
      request.meta["process"] = list2[i]
      request.meta["process_alias"] = list4[i]
      yield request

  def parse(self, response):
      version = response.meta["version"]
      process = response.meta["process"]
      process_alias = response.meta["process_alias"]
      
      div_tables = response.css('div.table-container')

      #表全てをlist化
      table = div_tables.css('td').getall()
      #listを成型
      rtable = []
      for sb in table:
        s = (re.sub("<a.*?>", "",sb).replace('</a>', ''))
        if '<td colspan="2">' in s:
          text = (s.replace('<td colspan="2">', '').replace('</td>', ''))
          rtable.append(text)
          rtable.append('')
        elif '<td colspan="3">' in s:
          text = (s.replace('<td colspan="3">', '').replace('</td>', ''))
          rtable.append(text)
          rtable.append('')
          rtable.append('')
        elif '<td>' in s:
          text = (s.replace('<td>', '').replace('</td>', ''))
          rtable.append(text)
        else:
          rtable.append(s)
      
      #listを分割
      def split_list(rtable, n):
        for idx in range(0, len(rtable), n):
          yield rtable[idx:idx + n]
      
      ntable = list(split_list(rtable, 5))
      
      #DB投入用に成型
      db = []
      for i in range(len(ntable)):
        dbh = [process, version]
        for j in range(5):
          dbh.insert(len(dbh), ntable[i][j])

        db.append(tuple(dbh))

      filename = "zabbix-parameters/" + process_alias + "_" + version + '.csv'
      with open(filename, 'w') as f:
          writer = csv.writer(f)
          writer.writerows(db)

      
      dynamodb_table = self.create_table(process_alias + "_" + version)

      for i in range(len(db)):
        data = {"Process": db[i][0], "Ver": db[i][1], "ParamName": db[i][2], "Mandatory": db[i][3], "ValRange": db[i][4], "ValDefault": db[i][5], "ParamDesc": db[i][6]}
        dynamodb_table.put_item(Item=data)
