<template lang="pug">
  v-app
    v-main
      v-toolbar(dense='')
        v-app-bar-nav-icon
        v-toolbar-title(@click="$router.push('/')") Technojaya
        v-spacer
      router-view
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
