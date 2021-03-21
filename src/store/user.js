
export default {
    namespaced: true,
    state: {
        data: null
    },
    mutations: {
        recoverUser (state) {
            let user = localStorage.getItem('user')
            if (user) {
                user = JSON.parse(user)
                state.data = user
            }
        },
        setUser (state, user) {
            state.data = user
            if (user) {
                localStorage.setItem('user', JSON.stringify(user))
            } else {
                localStorage.removeItem('user')
            }
        }
    }
}