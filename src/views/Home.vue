<template lang="pug">

  v-container
    .title.text-center Participants
    .content
      v-layout.my-6(v-if="isLoading")
        v-row.fill-height(align="center" justify="center")
          v-progress-circular(indeterminate color="primary" size="50")
      .clients(v-else)
        .empty-list.text-center(v-if="clients.length == 0")
          div List is empty
        .list(v-else)
          div(v-for="client in clients" :key="client.id")
            v-card.mx-auto.mt-6(color='#26c6da' dark='' max-width='400')
              v-card-actions
                v-list-item.grow
                  v-list-item-avatar(color='grey darken-3')
                    v-img.elevation-6(alt='' src='https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light')
                  v-list-item-content
                    v-list-item-title {{ client.first_name }} {{ client.last_name }}

              v-card-text.text-h5.font-weight-bold(v-for="post in client.posts" :key="post.id") "{{ post.text }}"
          //- div {{ clients }}
</template>

<script>
export default {
  data () {
    return {
      isLoading: false,
      title: 'Technojaya',
      clients: []
    }
  },
  mounted () {
    console.log('page mounted')
    this.getClientList()
  },
  methods: {
    getClientList () {
      this.isLoading = true
      this.$axios.get('/clients/')
        .then((resp) => {
          this.clients = resp.data
        })
        .finally (() => {
          this.isLoading = false
        })
    }
  }
}
</script>

<style scoped>

</style>