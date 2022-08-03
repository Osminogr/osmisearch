<template>
  <div class="search">    <div class="container">
        <h1>Osmisearch</h1>
    </div>
    <form class="search-form">
        <div class="input-group"><span class="input-group-text"><i class="fa fa-search"></i></span><input v-model="msg" class="form-control" type="text" placeholder="I am looking for.."></div>
    </form>
    <div class="container">
        <div class="row"><div class="col-md-2">
    <p class="o_heading">Categories</p>
    <div data-reflow-type="category-list" data-reflow-layout="unstyled">
        <div class="reflow-category-list ref-unstyled">
            <ul class="ref-categories">
                <li class="ref-category"><span>A Category</span></li>
                <li class="ref-category"><span>Aut Category</span></li>
                <li class="ref-category"><span>Hic Category</span></li>
            </ul>
        </div>
    </div>
</div><div class="col-md-10">
    <p class="o_heading">Search results</p>
    <div class="row product-list">

        <div class="col-sm-6 col-md-4 product-item" v-for="item in resp">
            <div class="product-container">
                <div class="row">
                    <div class="col-md-12"><a class="product-image" :href="item.link"><img :src="item.image_link" /></a></div>
                </div>
                <div class="row">
                    <div class="col-8">
                        <h2><a href="#">{{item.title}}</a></h2>
                    </div>
                    <div class="col-4"><a class="small-text" href="#">compare </a></div>
                </div>
                <div class="product-rating"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-half"></i><a class="small-text" href="#">82 reviews</a></div>
                <div class="row">
                    <div class="col-12">
                        <p class="product-description">{{item.description}}</p>
                        <div class="row">
                            <div class="col-6"><button class="btn btn-light" type="button">Buy Now!</button></div>
                            <div class="col-6">
                                <p class="product-price">{{item.price}} {{item.currency_code}} </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div></div>
    </div></div>
  
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      url: 'http://84.252.129.108:8000/search/1?q=',
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
#search_input {
  border: 0;
}
#input-group {
  border: 2px gray solid;
}
.search_icon {
  height: 100%;
}
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
.img_tov {
  width: 10em;
  height: 10em;
  border-radius: 10%;
  border: #42b983 2px solid;
}
</style>
