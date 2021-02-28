<template lang="pug">
  .home
    v-container
      v-row(no-gutters)

        // vuetify
        v-col.px-4
          div vuetify:
          h1.red--text.accent-3.black  This is home page
          div.caption.font-weight-bold saya bold
          v-card.mx-auto.mt-4(max-width="344" shaped)
            //- v-img(:src="require('@/assets/image.jpg')" height="200px")
            v-img(src="/cat.jpg" height="200px")
            v-card-title
              | Top western road trips
            v-card-subtitle
              | 1,000 miles of wonder
            v-card-actions
              v-btn(color="orange lighten-2" text)
                | Explore : {{ show }}
              v-spacer
              v-btn(icon @click="show = !show")
                v-icon {{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}
            v-expand-transition
              div(v-show='show')
                v-divider
                v-card-text
                  | I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.

        v-divider(vertical)

        // non vuetify
        v-col(style="padding-left:16px; padding-right:16px;")
          div non-vuetify:
          h1(style="color: #F44336; background-color: #000000") This is home page
          div(style="font-weight: bold; font-size: 12px") saya bold
</template>

<script>
  export default {
    data: () => ({
      show: false,
    }),
  }
</script>

<style scoped>

</style>