import axios from 'axios'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import SQLTable from '@/components/SQLTable.vue'
// import 'vue-awesome/icons'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

/* eslint-disable */

Vue.use(BootstrapVue)
Vue.component('sqltable', SQLTable)

Vue.config.productionTip = false

const OK = 1;

const vue = new Vue({
  delimiters: ['[[', ']]'],
  data: {
    input: "",
    output: "",
    tables: [],
    history: [],
  },
  computed: {
    reversedHistory() {
      return Object.values(this.history).reverse();
    }     
  },
  methods: {
    clearHistory: function () {
      this.history = [];
    },
    sendQuery: function () {
      this.history.push(this.input);
      axios.post('/query', this.input) //http://httpbin.org/post
        .then((response) => {
          this.output = JSON.stringify(response.data);
          var data = response.data;
          this.tables = [];
          if ((data.code || 0) === OK && data.result) {
            for (var result of data.result) {
              var columns = result.columns.map(column => column.name);
              this.tables.push({
                name: result.name,
                columns: columns,
                data: result.records.map(
                    record => record.reduce((map, obj, i) => (map[columns[i]] = obj, map), {})
                  ),
              });
            }
          } else {
            this.tables.push({
              name: '',
              columns: ["error"],
              data: [{error:data}],
            });
          }
        })
    }
  }
})
vue.$mount('#app')

