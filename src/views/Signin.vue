<template lang="pug">
  .signin
    v-container(style="max-width:600px")
      v-card.pa-4.text-center.my-12
        v-form(ref="form")
          h1 Login
          v-text-field.mt-4(v-model="email" outlined placeholder="Insert email" dense :rules="rules.email")
          v-text-field(v-model="password" outlined placeholder="Insert password" dense :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'" :rules="rules.password")
          v-btn.mb-4.primary(block @click="submitLogin" :loading="isLoading") Submit

        v-divider.my-4
        div # DEBUG #
        div email: {{ email }}
        div password: {{ password }}
        div stored vuex: {{ $store.state.user.data }}
</template>

<script>
export default {
  data () {
    return {
      email: 'technojaya14022021@gmail.com',
      password: '',
      showPassword: false,
      isLoading: false,
      rules: {
        email: [
          value => !!value || 'Email is required.',
          value => value.length >= 8 || 'Min 8 characters',
        ],
        password: [
          value => !!value || 'Password is required.',
          value => value.length >= 8 || 'Min 8 characters',
        ]
      },
    }
  },
  methods: {
    submitLogin () {
      if (!this.$refs.form.validate()) {
        return
      }
      this.isLoading = true
      const data = {
        email: this.email,
        password: this.password
      }
      this.$axios.post('https://api.inquiry.my/v1.0/merchants/me/login/', data)
        .then((resp) => {
          console.log(resp)
          this.data = resp.data
          this.$store.commit('user/setUser', resp.data)
          this.$router.push('/')
        })
        .finally (() => {
          this.isLoading = false
        })
    }
  }
}
</script>
