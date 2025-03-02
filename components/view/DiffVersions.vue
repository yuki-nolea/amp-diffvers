<template>
  <div class="content flex flex-col w-full max-h-full m-0 p-1 overflow-auto">
    <div class="grid grid-rows-2 grid-cols-2 pt-[20px] px-[20px]">
      <div class="row-start-1 col-start-1 col-span-2 flex gap-12 mb-5">
        <div class="flex items-center gap-2">
          <label for="process">Process : </label>
          <USelect label="Process : " name="process" v-model="process" icon="material-symbols:explosion-outline" class="w-[fit-content] ml-2" placeholder="Process:" :options="process_ops" />      
        </div>
        <div class="flex items-center gap-2">
          <label for="filter">Filter : </label>
          <USelect name="filter" v-model="filter" icon="material-symbols:filter-alt-outline" class="w-[fit-content] ml-2" placeholder="Filter:" :options="filter_ops" />      
        </div>
      </div>

      <div class="flex items-center row-start-2 row-span-1 col-start-1">
        <label for="left-version">Ver : </label>
        <USelect name="left-version" v-model="left_version" icon="system-uicons:versions" class="w-[fit-content] ml-2" placeholder="Version:" :options="version_ops" />
      </div>
      
      <div class="flex items-center row-start-2 row-span-1 col-start-2">
        <label for="right-version">Ver : </label>
        <USelect name="right-version" v-model="right_version" icon="system-uicons:versions" class="w-[fit-content] ml-2" placeholder="Version:" :options="version_ops" />
      </div>
    </div>

    <UDivider />
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

  const str = await useFetch('/api/params', 
    {
      onRequest({request, options})
      {
        options.headers.set('Authorization', session.tokens!.idToken!.toString())
      },
      onResponseError(error)
      {
        throw showError({ statusCode: error.response.status, statusMessage: error.response.statusText });
      }
    }
  );


  const response = 
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
  };

  const duplex = (arr: any) => {
    const ret = [];
    for(const item of arr)
    {
      ret.push([{...item}])
      ret[ret.length - 1].push({...item})
    }

    return ret;
  }

  const alls = duplex(response.data);
  const matches = duplex(response.data);
  const differences = duplex(response.data);

  console.log(alls);

  const filtered_params = computed(() =>
  {
    if(filter.value == "None") return alls;
    else if(filter.value == "Match") return matches;
    else return differences;
  });

  const filter_ops =  [{ label: "None", value: "None" }, { label: "Match", value: "Match" }, { label: "Difference", value: "Difference" }];
  const filter = ref();

  const process_ops = 
  [
    { label: "Zabbix server", value: "Zabbix server" },{ label: "Zabbix proxy", value: "Zabbix proxy" },{ label: "Zabbix agent (UNIX)", value: "Zabbix agent (UNIX)" },
    { label: "Zabbix agent2 (UNIX)", value: "Zabbix agent2 (UNIX)" },{ label: "Zabbix agent (Windows)", value: "Zabbix agent (Windows)" }
  ];
  const process = ref();
  
  const version_ops =  [{ label: "6.0", value: "6.0" },{ label: "5.0", value: "5.0" },{ label: "4.0", value: "4.0" }];
  const left_version = ref(version_ops[0].value);
  const right_version = ref(version_ops[0].value);

  const { toggle } = useToggleParam();
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