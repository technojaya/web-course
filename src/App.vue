<template lang="pug">
  v-app
    v-main
      v-toolbar(dense='')
        v-app-bar-nav-icon
        v-toolbar-title(@click="$router.push('/')") Technojaya
        v-spacer
        v-btn(v-if="$store.state.user.data" small @click="clickLogout") Log out
        v-btn(v-else small @click="$router.push('/signin')") Log in
      router-view
      v-footer(color='primary lighten-1' padless='')
        v-row(justify='center' no-gutters='')
          v-btn.my-2(v-for='link in links' :key='link' color='white' text='' rounded='')
            | {{ link }}
          v-col.primary.lighten-2.py-4.text-center.white--text(cols='12')
            | {{ new Date().getFullYear() }} — 
            strong Vuetify
</template>

<script>
  export default {
    data () {
      return {
        links: [
          'Home',
          'About Us',
          'Team',
          'Services',
          'Blog',
          'Contact Us',
        ],
      }
    },
    mounted () {
      this.$store.commit('user/recoverUser')
    },
    methods: {
      clickLogout () {
        this.$store.commit('user/setUser', null)
      }
    }
  }
</script>

<style lang="scss">
</style>
