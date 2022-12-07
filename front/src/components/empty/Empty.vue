<template>
  <div>
    <a-empty
    image="https://gw.alipayobjects.com/mdn/miniapp_social/afts/img/A*pevERLJC9v0AAAAAAAAAAABjAQAAAQ/original"
    :image-style="{
      height: '60px',
    }"
  >
    <template #description>
      <h2>{{$t('content')}}</h2>
      <span>{{$t('description')}}</span>
    </template>
  </a-empty>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    name: 'Empty',
    i18n: require('./i18n'),
    data() {
      return {
      }
    },
    computed: {
      ...mapState('setting', ['pageMinHeight']),
      desc() {
        return this.$t('description')
      }
    }
  }
</script>

<style scoped lang="less">
@import "index";
</style>