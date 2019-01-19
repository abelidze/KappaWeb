const OK = 1;

const app = new Vue({
  delimiters: ['[[', ']]'],
  data: {
    input: "",
    output: "",
    tables: [],
  },
  methods: {
    sendQuery: function () {
      axios.post('http://localhost:8000/query', this.input) //http://httpbin.org/post
        .then((response) => {
          this.output = JSON.stringify(response.data);
          var data = response.data;
          this.tables = [];
          if (handleResponse(data.code || 0) && data.result) {
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
}).$mount('#app')
// {
//   name: 'test-table',
//   columns: ['id', 'year'],
//   code: 1,
//   rows: [{ id: 1, year: 1 }]
// }


function handleResponse(code) {
  if (code === OK)
    return true;
  alert("Query failed");
  return false;
}
