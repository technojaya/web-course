<template lang="pug">
  .home-page

    v-carousel(hide-delimiters='')
      v-carousel-item(v-for='(item,i) in items' :key='i' :src='item.src')
    v-container.text-center
      h1 Welcome Technojaya

</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
        ]
      }
    },
  }
</script>

<style scoped>

</style>