<template>
  <div class="
    grid grid-rows-[1fr] grid-cols-[158px_96px_158px_1fr] 
    shadow-[0_1px_3px_rgba(0,0,0,0.12),_0_1px_2px_rgba(0,0,0,0.24)]
    transition-all duration-300 ease-[cubic-bezier(.25,.8,.25,1)]
    h-full w-full bg-[#fff] text-sm rounded-sm p-0"
  >
    <div :class="classObject(nameDiff)" class="name param_cell col-start-1 p-1" data-id="" v-html="name"></div>
    <div v-if="coin == 1" :class="classObject(mandatoryDiff)" class="mandatory param_cell col-start-2 p-1" data-id="" v-html="mandatory"></div>
    <div v-if="coin == 1" :class="classObject(rangeDiff)" class="range param_cell col-start-3 p-1" data-id="" v-html="range"></div>
    <div v-if="coin == 1" :class="classObject(defaultDiff)" class="default param_cell col-start-4 p-1" data-id="" v-html="default"></div>
    <div v-if="coin == 0" :class="classObject(descriptionDiff)" class="description param_cell col-start-2 col-span-3 p-1" data-id="" v-html="description"></div>
  </div>
</template>

<script lang="ts" setup>
  
  const props = defineProps<{
    name: string, nameDiff: string,
    mandatory: string, mandatoryDiff: string,
    range: string, rangeDiff: string,
    default: string, defaultDiff: string,
    description: string, descriptionDiff: string
  }>();

  const { coin } = useToggleParam();
  const classObject = (diffMsg: string) => ({ match:  diffMsg == "match", difference: diffMsg == "difference", alone: diffMsg == "alone", none: diffMsg == "none" });
</script>

<style scoped>
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

  .match
  {
    color: black;
    /* background-color: aqua; */
  }

  .difference
  {
    color: white;
    background-color: oklch(0.577 0.245 27.325);
  }

  .alone
  {
    color: white;
    background-color: #0DDF08;
  }

  .none
  {
    color: white;
    background-color: #D9D9D9;
    text-decoration: line-through;
  }

</style>