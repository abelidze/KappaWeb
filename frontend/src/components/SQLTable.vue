<template>
  <table :name='name'>
    <thead>
      <tr>
        <th v-for="key in columns"
            :key="key"
            :class="{ active: sortKey == key }"
            @click="sortBy(key)"
            >
                {{ key | capitalize }}
                <span class="arrow" :class="sortOrders[key] > 0 ? 'asc' : 'dsc'"></span>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="entry in filteredData" :key="entry">
        <td v-for="key in columns" :key="key">
            {{ entry[key] }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'sqltable',
  props: {
    data: Array,
    columns: Array,
    filterKey: {
      type: String,
      default: ''
    }
  },
  data: function () {
    var sortOrders = {}
    this.columns.forEach(function (key) {
      sortOrders[key] = 1
    })
    return {
      name: '',
      sortKey: '',
      sortOrders: sortOrders
    }
  },
  computed: {
    filteredData: function () {
      var sortKey = this.sortKey
      var filterKey = this.filterKey && this.filterKey.toLowerCase()
      var order = this.sortOrders[sortKey] || 1
      var data = this.data
      if (filterKey) {
        data = data.filter(function (row) {
          return Object.keys(row).some(function (key) {
            return String(row[key]).toLowerCase().indexOf(filterKey) > -1
          })
        })
      }
      if (sortKey) {
        data = data.slice().sort(function (a, b) {
          a = a[sortKey]
          b = b[sortKey]
          return (a === b ? 0 : a > b ? 1 : -1) * order
        })
      }
      return data
    }
  },
  filters: {
    capitalize: function (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }
  },
  methods: {
    sortBy: function (key) {
      this.sortKey = key
      this.sortOrders[key] = -this.sortOrders[key]
    }
  }
};
</script>

<style lang="scss">

$header-background-color: #263238;
$primary-color: #1E88E5;
$primary-color-light: lighten($primary-color, 10%);
$primary-color-dark: darken($primary-color, 20%);
$inactive-color: #AFB3B5;
$inactive-color-light: lighten($inactive-color, 20%);

$font-link: 'https://fonts.googleapis.com/css?family=Noto+Sans:400,700';
$font: "Noto Sans", sans-serif;

@mixin hover-links {
  background     : $primary-color;
  color          : #fff;
  text-decoration: none;
  font-weight    : auto;
}

@import url(#{$font-link});

input:not([type]),
input[type=number],
input[type=password],
input[type=search],
input[type=text] {
  padding      : 8px;
  border       : 1px solid rgba(0,0,0,.12);
  border-radius: 2px;
  font-size    : 15px;
}

input[type=search]:first-child {
  box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.2), 0 1px 5px 0 rgba(0,0,0,0.12);
}

input[type=submit] {
  padding       : 0 16px;
  min-width     : 64px;
  height        : 36px;
  border        : none;
  border-radius : 2px;
  background    : $primary-color;
  box-shadow    : 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
  color         : #fff;
  text-transform: uppercase;
  font-size     : 14px;
  cursor        : pointer;
  transition    : all .2s;
}

input[type=submit]:hover {
  background: $primary-color-dark;
}

input[type=button][disabled],
input[type=submit][disabled] {
  background: $inactive-color!important;
  color     : invert($inactive-color);
  cursor    : no-drop;
}

div input[name=delete],
div input[name=drop],
div input[name=truncate],
input[value=Kill] {
  background: repeating-linear-gradient(-55deg, $primary-color, $primary-color 5px, $primary-color-light 5px, $primary-color-light 10px);
  transition: all .2s;

  &:hover {
    background: repeating-linear-gradient(-55deg, $primary-color-dark, $primary-color-dark 5px, $primary-color 5px, $primary-color 10px);
  }
}

input[type=checkbox] {
  display            : inline-block;
  padding-left       : 25px;
  height             : 20px;
  outline            : 0;
  background-position: 0 0;
  background-size    : 20px;
  background-repeat  : no-repeat;
  vertical-align     : middle;
  font-size          : 20px;
  line-height        : 20px;
  cursor             : pointer;
  -webkit-appearance : none;
  -webkit-user-select: none;
  user-select        : none;
}

input[type=checkbox]:checked {
  background-position: 0 -20px;
}

input[type=radio] {
  display            : inline-block;
  padding-left       : 25px;
  height             : 20px;
  outline            : 0;
  background-position: 0 0;
  background-size    : 20px;
  background-repeat  : no-repeat;
  vertical-align     : middle;
  font-size          : 20px;
  line-height        : 20px;
  cursor             : pointer;
  -webkit-appearance : none;
  -webkit-user-select: none;
  user-select        : none;
}

input[type=radio]:checked {
  background-position: 0 -21px;
}

input[type=number] {
  padding: 8px;
}

#tables {
  overflow-x   : hidden!important;
  margin-bottom: 47px;
  padding      : 9px 12px 0 6px;
  flex         : 1;

  .select:hover {
    @include hover-links;
  }

  a {
    display      : inline-block;
    overflow     : hidden;
    padding      : 6px 0 6px 8px;
    width        : 175px;
    border-radius: 2px;
    text-overflow: ellipsis;
    transition   : all .2s;
    color        : #000;

    &:hover {
      background     : $inactive-color-light;
      color          : #000;
      text-decoration: none;
    }

    &.select {
      position      : relative;
      float         : right;
      padding       : 5px;
      width         : auto;
      border-radius : 2px;
      background    : #fff;
      color         : $primary-color;
      text-align    : center;
      text-transform: uppercase;
      font-weight   : bold;
      font-size     : 13px;
      line-height   : 18px;
    }

  }
}

#table, .table {
  padding: 0 24px;

  table {
    width: 100%;
  }
}

textarea {
  outline: none;
  resize: vertical;
  min-height: 160px;
  max-height: 640px;
}


table {
  margin-top     : 20px;
  min-width      : 800px;
  border-collapse: collapse;
  box-shadow     : 0 1px 4px rgba(88, 88, 88, 0.01), 0 2px 3px rgba(88, 88, 88, 0.26);
  white-space    : nowrap;
  font-size      : 13px;
  order          : 4;
}

thead td,
thead th {
  background: #ececec;
  position  : sticky;
  top       : 0;
  z-index   : 2;

  &:before {
    content   : '';
    position  : absolute;
    background: #fafafa;
    top       : -20px;
    left      : -10px;
    width     : 120%;
    height    : 20px;
  }

  &:after {
    content      : '';
    position     : absolute;
    left         : 0;
    bottom       : 0;
    width        : 100%;
    border-bottom: 1px solid #cecece;
  }
}

thead th {
  padding   : 0 18px;
  text-align: left;
}

th {
  box-sizing : border-box;
  padding    : 5px 18px !important;
  width      : 20%;
  border     : 1px solid #ececec;
  background : #fff;
  font-weight: normal;
  font-size  : 14px;
  .active{
    .arrow {
      opacity: 1;
    }
  }
}

td {
  box-sizing: border-box;
  padding   : 2px 10px 0;
  height    : 45px;
  border    : 1px solid #ececec;
  background: #fff;
  color     : #000;
}

span.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-right: 5px;
  opacity: 1;
    .asc {
      border-left: 4px solid transparent;
      border-right: 4px solid transparent;
      border-bottom: 4px solid rgb(10, 86, 124);
    }

    .dsc {
      border-left: 4px solid transparent;
      border-right: 4px solid transparent;
      border-top: 4px solid rgb(10, 86, 124);
    }  
}
  
.odd td,
.odd th {
  background: #fafafa;
}

td a,
td a:visited,
th a,
th a:visited {
  color      : $primary-color;
  font-weight: 700;
}

.js .checkable .checked td,
.js .checkable .checked th {
  background: #e0e0e0;
}

</style>