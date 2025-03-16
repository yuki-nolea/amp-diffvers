import csv from 'csvtojson'

export default defineEventHandler(async (event) =>
{
  const params = [];
  for(const file of files)
  {
    const arr = await csv().fromString(file);
    params.push(...arr);
  }

  return JSON.stringify(params);
})


const files = 
[
`process,version,description
"Zabbix server", "6.0", 'ZabbixDBの各テーブルの文字コードをutf8mb4へ変換することが推奨されている。変換方法は<a href="https://www.zabbix.com/documentation/6.0/jp/manual/appendix/install/db_charset_coll">2 Zabbixデータベースのキャラクターセットと照合の修正</a>を参照',
"Zabbix server", "6.0", 'History系テーブルにプライマリキーが追加された。ただのデータ移行ではプライマリキーは自動追加されないため、<strong>手動で追加する</strong>必要がある。方法は<a href="https://www.zabbix.com/documentation/6.0/jp/manual/appendix/install/db_primary_keys">3 データベースの主キーのアップグレード</a>参照',
"Zabbix server", "6.0", "ポジショナルマクロが撤廃された。手動変換しないとアイテムの名前がキーの引数の名前に変換されず”$1”などと表示されてしまう。公式にてポジショナルマクロ変換スクリプトが提供されているが、ベーシックサポート以上の契約が必要",
"Web interface", "4.0", "Zabbix Server の“SenderFrequencyパラメータ”が撤廃されたため、代わりに、Webインターフェースからメディアタイプを選択し、オプションの”試行間隔”に値を設定する必要がある。"`
]






