<template>
  <div class="content p-4  ">
    <div class="param-row flex gap-3 m-1" v-for="item in notes">
      <div class="param-card
        grid grid-rows-[1fr] grid-cols-[158px_96px_1fr] 
        shadow-[0_1px_3px_rgba(0,0,0,0.12),_0_1px_2px_rgba(0,0,0,0.24)]
        transition-all duration-300 ease-[cubic-bezier(.25,.8,.25,1)]
        h-full w-full bg-[#fff] text-sm rounded-sm p-2"
      >
        <div class="name param_cell col-start-1 p-1" data-id="" v-html="item.process"></div>
        <div class="mandatory param_cell col-start-2 p-1" data-id="" v-html="item.version"></div>
        <div class="range param_cell col-start-3 p-1" data-id="" v-html="item.description"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { fetchAuthSession } from 'aws-amplify/auth';

  const session = await fetchAuthSession();
  const ret = await useFetch('/api/note', 
  {
    onRequest({request, options}) { options.headers.set('Authorization', session.tokens!.idToken!.toString()); },
    onResponseError(error) { throw showError({ statusCode: error.response.status, statusMessage: error.response.statusText }); }
  });
  const data = JSON.parse(ret.data.value!);
  console.log(data)

  const notes = ref(data.map((item: any) => ({process: item.process, version: item.version, description: item.description})));

</script>



<style scoped>
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
  .param_cell
  {
    border-right: 1px solid #E0E0E0;
    text-align: center;
    overflow-wrap: break-word;

    transition-property: display, opacity, height, padding-top;
    transition-duration: 0.3s;
    @starting-style {
      height: 0px;
      opacity: 0;
    }
  }
</style>