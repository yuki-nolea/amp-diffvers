<template>
  <div class="content flex flex-col w-full max-h-full m-0 p-1 overflow-y-auto overflow-x-clip">
    <div class="grid grid-rows-2 grid-cols-2 pt-[20px] px-[20px]">
      <div class="row-start-1 col-start-1 col-span-2 flex gap-12 mb-5">
        <div class="flex items-center gap-2">
          <label for="process">Process : </label>
          <USelect label="Process : " name="process" v-model="process" icon="material-symbols:explosion-outline" class="w-[fit-content] ml-2" :options="process_ops" :value="process"/>      
        </div>
        <div class="flex items-center gap-2">
          <label for="filter">Filter : </label>
          <USelect name="filter" v-model="filter" icon="material-symbols:filter-alt-outline" class="w-[fit-content] ml-2" :options="filter_ops" :value="filter"/>      
        </div>
      </div>

      <div class="flex items-center row-start-2 row-span-1 col-start-1">
        <label for="left-version">Ver : </label>
        <USelect name="left-version" v-model="left_version" icon="system-uicons:versions" class="w-[fit-content] ml-2" placeholder="Version:" :options="version_ops" :value="left_version" />
      </div>
      
      <div class="flex items-center row-start-2 row-span-1 col-start-2">
        <label for="right-version">Ver : </label>
        <USelect name="right-version" v-model="right_version" icon="system-uicons:versions" class="w-[fit-content] ml-2" placeholder="Version:" :options="version_ops" :value="right_version" />
      </div>
    </div>

    <UDivider class="w-full" />
    <div class="grow m-4 mb-12">
      <div class="param-row flex gap-3">
        <div class="param-card w-full">
          <WidgetRow :name="`名前`" :name-diff="`match`" :mandatory="`必須`" :mandatory-diff="`match`" :range="`範囲`" :range-diff="`match`" :default="`デフォルト`" :default-diff="`match`" :description="`説明`" :description-diff="`match`" />
        </div>
        <div class="param-card  w-full">
          <WidgetRow :name="`名前`" :name-diff="`match`" :mandatory="`必須`" :mandatory-diff="`match`" :range="`範囲`" :range-diff="`match`" :default="`デフォルト`" :default-diff="`match`" :description="`説明`" :description-diff="`match`" />
        </div>
      </div>
      
      
      <div class="param-row flex gap-3" v-for="item in filtered_params">
        <div class="param-card w-full">
          <WidgetRow :name="item[0].name" :name-diff="item[0].nameDiff" :mandatory="item[0].mandatory" :mandatory-diff="item[0].mandatoryDiff" :range="item[0].range" :range-diff="item[0].rangeDiff" 
            :default="item[0].default" :default-diff="item[0].defaultDiff" :description="item[0].description" :description-diff="item[0].descriptionDiff" />
        </div>
        <div class="param-card  w-full">
          <WidgetRow :name="item[1].name" :name-diff="item[1].nameDiff" :mandatory="item[1].mandatory" :mandatory-diff="item[1].mandatoryDiff" :range="item[1].range" :range-diff="item[1].rangeDiff" 
            :default="item[1].default" :default-diff="item[1].defaultDiff" :description="item[1].description" :description-diff="item[1].descriptionDiff" />        </div>
      </div>

      <UButton class="fixed bottom-9 right-6" icon="material-symbols:360" size="xl" color="black" :ui="{ rounded: 'rounded-full' }" @click="toggle" />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { fetchAuthSession } from 'aws-amplify/auth';

  const session = await fetchAuthSession();
  const ret = await useFetch('/api/params', 
  {
    onRequest({request, options}) { options.headers.set('Authorization', session.tokens!.idToken!.toString()); },
    onResponseError(error) { throw showError({ statusCode: error.response.status, statusMessage: error.response.statusText }); }
  });
  const all_params = JSON.parse(ret.data.value!);

  const filter_ops =  [{ label: "None", value: "None" }, { label: "Match", value: "Match" }, { label: "Difference", value: "Difference" } ];
  const filter = ref(filter_ops[0].label);

  const process_ops = [ { label: "Zabbix server", value: "Zabbix server" },{ label: "Zabbix agent (UNIX)", value: "Zabbix agent (UNIX)" } ];
  const process = ref(process_ops[0].label);
  
  const version_ops =  [{ label: "6.0", value: "6.0" },{ label: "5.0", value: "5.0" },{ label: "4.0", value: "4.0" }];
  const left_version = ref(version_ops[1].label);
  const right_version = ref(version_ops[0].label);

  const { toggle } = useToggleParam();


  
  const left_params: any[] = all_params.filter((item: any) => item.process == process && item.version == left_version.value);
  const right_params: any[] = all_params.filter((item: any) => item.process == process && item.version == right_version.value);
  const filtered_params = ref()
  watchEffect(() =>
  {
    left_params.splice(0, left_params.length, ...all_params.filter((item: any) => item.process == process.value && item.version == left_version.value));
    right_params.splice(0, right_params.length, ...all_params.filter((item: any) => item.process == process.value && item.version == right_version.value));

    left_params.forEach((item: any) => { item.nameDiff = "match"; item.mandatoryDiff = "match"; item.rangeDiff = "match"; item.defaultDiff = "match"; item.descriptionDiff = "match"; })
    right_params.forEach((item: any) => { item.nameDiff = "match"; item.mandatoryDiff = "match"; item.rangeDiff = "match"; item.defaultDiff = "match"; item.descriptionDiff = "match"; })

    for(const item of left_params)
    {
      const same = right_params.find((ritem: any) => item.name == ritem.name);
      if(same) 
      {
        if(item.name != same.name) {item.nameDiff = "difference"; same.nameDiff = "difference"; }
        if(item.mandatory != same.mandatory) {item.mandatoryDiff = "difference"; same.mandatoryDiff = "difference"; }
        if(item.range != same.range) {item.rangeDiff = "difference"; same.rangeDiff = "difference"; }
        if(item.default != same.default) {item.defaultDiff = "difference"; same.defaultDiff = "difference"; }
        if(item.description != same.description) {item.descriptionDiff = "difference"; same.descriptionDiff = "difference"; }
      }
      else
      {
        item.nameDiff = "alone"; item.mandatoryDiff = "alone"; item.rangeDiff = "alone"; item.defaultDiff = "alone"; item.descriptionDiff = "alone";
        const new_param = {...item, nameDiff: "none", mandatoryDiff: "none", rangeDiff: "none", defaultDiff: "none", descriptionDiff: "none"};
        right_params.push(new_param);
      }
    }

    for(const item of right_params)
    {
      const same = left_params.find((ritem: any) => item.name == ritem.name);
      if(!same)
      {
        item.nameDiff = "alone"; item.mandatoryDiff = "alone"; item.rangeDiff = "alone", item.defaultDiff = "alone"; item.descriptionDiff = "alone";
        const new_param = {...item, nameDiff: "none", mandatoryDiff: "none", rangeDiff: "none", defaultDiff: "none", descriptionDiff: "none"};
        left_params.push(new_param);
      }
    }


    const comp = (a: string, b: string) => 
    {
      if(a == b) return 0;
      else if(a < b) return -1;
      else return 1;
    }

    left_params.sort((a: any, b: any) => comp(a.name, b.name));
    right_params.sort((a: any, b: any) => comp(a.name, b.name));

    const ret = []
    for(let i = 0; i<left_params.length; ++i)
    { 
      if(filter.value == "Match")
      {
        const item = left_params[i];
        if(item.nameDiff == "match" && item.mandatoryDiff == "match" &&  item.rangeDiff == "match" && item.defaultDiff == "match" && item.descriptionDiff == "match")
        {
          ret.push([left_params[i], right_params[i]]) 
        }
      }
      else if(filter.value == "Difference")
      {
        const item = left_params[i];
        if(item.nameDiff == "difference" || item.mandatoryDiff == "difference" ||  item.rangeDiff == "difference" || item.defaultDiff == "difference" || item.descriptionDiff == "difference" ||
          item.nameDiff == "alone" || item.mandatoryDiff == "alone" ||  item.rangeDiff == "alone" || item.defaultDiff == "alone" || item.descriptionDiff == "alone" ||
          item.nameDiff == "none" || item.mandatoryDiff == "none" ||  item.rangeDiff == "none" || item.defaultDiff == "none" || item.descriptionDiff == "none"
        )
        {
          ret.push([left_params[i], right_params[i]])
        } 
      }
      else ret.push([left_params[i], right_params[i]]) 
    }

    filtered_params.value = ret;
  })

  //console.log(filtered_params);

</script>



<style scoped>
  .content {
    --sb-thumb-color: #3c3c3c;
  }

  .content::-webkit-scrollbar {
    width: 4px;
  }

  .content::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0);
    border-radius: 11px;
  }

  .content::-webkit-scrollbar-thumb {
    background: rgba(60, 60, 60, 1);
    border-radius: 11px;
  }

  @supports not selector(::-webkit-scrollbar) {
    .content {
        scrollbar-color: var(--sb-thumb-color)
                      var(--sb-track-color);
    }
  }

  .param-row
  {
    margin-bottom: 8px;
  }

  .param-row:hover .param-card
  {
    box-shadow: 0 4px 7px rgba(0,0,0,0.25), 0 2px 2px rgba(0,0,0,0.22);
  }

  .param-card
  {
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }
</style>





<!-- const response = 
{
  data: [
  {
    process: "Zabbix server",
    version: "4.0",
    name: "MySQL/Percona", nameDiff: "match",
    mandatory: "どれか一つ", mandatoryDiff: "match",
    range: "8.0.X", rangeDiff: "match",
    default: "なし", defaultDiff: "match",
    description: "4 MySQL (または Percona) を Zabbix バックエンド データベースとして使用する場合に必要です。 InnoDB エンジンが必要です。 サーバー/プロキシの構築には MariaDB Connector/C ライブラリを使用することをお勧めします。",
    descriptionDiff: "match",
  },
  {
    process: "Zabbix server",
    version: "5.0",
    name: "MySQL/Percona", nameDiff: "match",
    mandatory: "どれか一つ", mandatoryDiff: "match",
    range: "8.0.X", rangeDiff: "match",
    default: "なし", defaultDiff: "match",
    description: "5 MySQL (または Percona) を Zabbix バックエンド データベースとして使用する場合に必要です。 InnoDB エンジンが必要です。 サーバー/プロキシの構築には MariaDB Connector/C ライブラリを使用することをお勧めします。",
    descriptionDiff: "match",
  },
  {
    process: "Zabbix server",
    version: "6.0",
    name: "MySQL/Percona", nameDiff: "match",
    mandatory: "どれか一つ", mandatoryDiff: "match",
    range: "8.0.X", rangeDiff: "match",
    default: "なし", defaultDiff: "match",
    description: "MySQL (または Percona) を Zabbix バックエンド データベースとして使用する場合に必要です。 InnoDB エンジンが必要です。 サーバー/プロキシの構築には MariaDB Connector/C ライブラリを使用することをお勧めします。",
    descriptionDiff: "match",
  },]
}; -->