<template>
  <div class="flex flex-col w-full h-full m-0 p-1" ref="wrapper">
    <div class="bg-orange-200 grid grid-rows-2 grid-cols-2 pt-[20px] px-[20px]">
      <div class="row-start-1 col-start-1 col-span-2">
        <div class="flex items-center gap-2">
          <label for="filter">Filter : </label>
          <USelect name="filter" v-model="filter" icon="material-symbols:filter-alt-outline" class="w-[fit-content] ml-2" placeholder="Filter:" :options="filter_ops" />      
        </div>

        <div class="flex items-center gap-2 mt-4">
          <label for="process">Process : </label>
          <USelect label="Process : " name="process" v-model="process" icon="material-symbols:explosion-outline" class="w-[fit-content] ml-2" placeholder="Process:" :options="process_ops" />      
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

    <div class="grow bg-gray-500">
      <div class="h-[800px] bg-orange-900 m-4 mb-12">
        <div class="flex my-[10px] mx-0 row_template ">
            <div class="param_card left_param_card">
                <div class="param_cell param_name mdl-data-table__cell--non-numeric" data-id="">名前</div>
                <div hidden class="param_cell mandatory display_group_0 mdl-data-table__cell--non-numeric" data-id="">必須</div>
                <div hidden class="param_cell val_range display_group_0 mdl-data-table__cell--non-numeric" data-id="">範囲</div>
                <div hidden class="param_cell val_default display_group_0 mdl-data-table__cell--non-numeric" data-id="">デフォルト</div>
                <div class="param_cell param_desc display_group_1 mdl-data-table__cell--non-numeric" data-id="">説明</div>
            </div>
            <div class="param_card right_param_card">
                <div class="param_cell param_name mdl-data-table__cell--non-numeric" data-id="">名前</div>
                <div hidden class="param_cell mandatory display_group_0 mdl-data-table__cell--non-numeric" data-id="">必須</div>
                <div hidden class="param_cell val_range display_group_0 mdl-data-table__cell--non-numeric" data-id="">範囲</div>
                <div hidden class="param_cell val_default display_group_0 mdl-data-table__cell--non-numeric" data-id="">デフォルト</div>
                <div class="param_cell param_desc display_group_1 mdl-data-table__cell--non-numeric" data-id="">説明</div>
            </div>
        </div>
      </div>

      <UButton class="fixed bottom-9 right-6" icon="material-symbols:360" size="xl" color="black" :ui="{ rounded: 'rounded-full' }" />
    </div>
  </div>
</template>

<script setup lang="ts">
  const filter_ops = 
  [{
    label: "None",
    value: "None"
  },{
    label: "Match",
    value: "Match"
  },{
    label: "Difference",
    value: "Difference"
  }];
  const filter = ref();

  const process_ops = 
  [{
    label: "Zabbix server",
    value: "Zabbix server"
  },{
    label: "Zabbix proxy",
    value: "Zabbix proxy"
  },{
    label: "Zabbix agent (UNIX)",
    value: "Zabbix agent (UNIX)"
  },{
    label: "Zabbix agent2 (UNIX)",
    value: "Zabbix agent2 (UNIX)"
  },{
    label: "Zabbix agent (Windows)",
    value: "Zabbix agent (Windows)"
  }];
  const process = ref();
  
  const version_ops = 
  [{
    label: "6.0",
    value: "6.0"
  },{
    label: "5.0",
    value: "5.0"
  },{
    label: "4.0",
    value: "4.0"
  }];
  const left_version = ref(version_ops[0].value);
  const right_version = ref(version_ops[0].value);

  const wrapper = ref();
  const onResize = () =>
  {
    console.log(wrapper.value.getBoundingClientRect().height)
  };

  onMounted(() =>
  {
    window.addEventListener('resize', onResize);
  });

  onUnmounted(() =>
  {
    window.removeEventListener('resize', onResize)
  });
</script>

<style scoped>
  .content
  {
    background-color:aqua;
  }
</style>