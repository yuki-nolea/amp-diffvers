import fs from 'fs'
import path from 'path'
import csv from 'csvtojson'

const files = 
[
  'public/params/ZabbixAgent_UNIX_4.0.csv',
  'public/params/ZabbixAgent_UNIX_5.0.csv',
  'public/params/ZabbixAgent_UNIX_6.0.csv',
  'public/params/ZabbixServer_4.0.csv',
  'public/params/ZabbixServer_5.0.csv',
  'public/params/ZabbixServer_6.0.csv',
];

export default defineEventHandler(async (event) =>
{

  const params = [];
  for(const file of files)
  {
    const arr = await csv().fromFile(file);
    params.push(...arr);
  }

  console.log(params)
  return JSON.stringify(params);
})

