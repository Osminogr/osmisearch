<template>
  <div class="hello">
    <input v-model="msg"/>
    <br>
    <div class="container">
      <ul>
        <li v-for="item in resp" class="card col" style="width: 18rem;">
          <img class="card-img-top img-fluid" :src="item.image_link" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">{{item.title}}</h5>
            <p class="card-text"></p>
            <a :href="item.link" class="btn btn-primary">Перейти
            </a>
          </div>
        </li>
      </ul>
    </div>

    <div class="error_area">
    {{resp}}
  </div>
  </div>
  
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      url: 'http://127.0.0.1:8000/search/1?q=',
      msg: '',
      resp: this.$axios
      .get(this.url + this.msg)
      .then(response => (this.resp = response.data))
    }
  },
  watch: {
    msg: function (val) {
      this.$axios
      .get(this.url+ this.msg)
      .then(response => (this.resp = response.data))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
img {
  width: 10em;
  height: 10em;
  border-radius: 10%;
  border: #42b983 2px solid;
}
</style>
