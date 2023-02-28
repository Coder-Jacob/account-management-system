var app_aaa = new Vue({
    el: '#app',
    data: {
    },
    methods: {
        open_aa(){
            console.log('aaa')
            this.$notify({
                title: 'tit',
                message: 'msg',
                type: 'typ'
            });
        }
    },
});