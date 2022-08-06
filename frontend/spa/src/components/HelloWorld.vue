<template>
  <div class="search">    <div class="container">
        <h1>Osmisearch</h1>
    </div>
    <form class="search-form">
        <div class="input-group"><span class="input-group-text"><i class="fa fa-search"></i></span><input v-model="msg" class="form-control" type="text" placeholder="I am looking for.."></div>
    </form>
      <p v-if="sugg.suggest">Возможно, вы имели ввиду <b>{{sugg.suggest}}</b></p>
    <div class="container">
        <div class="row"><div class="col-md-2">
    <p class="o_heading">Categories</p>
    <div data-reflow-type="category-list" data-reflow-layout="unstyled">
        <div class="reflow-category-list ref-unstyled">
            <ul class="ref-categories" >
                <li class="ref-category" v-for="category in u_categories" >
                <input type="checkbox"  :id="category.code" :value="category.code" v-model="selected_categories"/>
                <span>{{category.title}}</span></li>
            </ul>
        </div>
    </div>
</div><div class="col-md-10">
    <p class="o_heading">Search results</p>
    <div class="row product-list">

        <div class="col-sm-6 col-md-4 product-item" v-for="item in filtered_items">
            <div class="product-container">
                <div class="row">
                    <div class="col-md-12"><a class="product-image" :href="item.link"><img :src="item.image_link" /></a></div>
                </div>
                <div class="row">
                    <div class="col-8">
                        <h2><a href="#">{{item.title}}</a></h2>
                    </div>
                    <div class="col-4"><a class="small-text" href="#">{{item.category.title}} </a></div>
                </div>
                <div class="product-rating"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-half"></i><a class="small-text" href="#">82 reviews</a></div>
                <div class="row">
                    <div class="col-12">
                        <p class="product-description">{{item.description}}</p>
                        <div class="row">
                            <div class="col-6"><button class="btn btn-light" type="button" >Bu</button></div>
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
      url: 'http://localhost:8000/',
      msg: '',
      sugg:'',
      resp: [],
      categories: [],
      selected_categories: [],
    }
  },
  computed:{
    u_categories: function (val) {
      this.categories = [];
        this.resp.forEach(item => {
          this.categories.push(item.category)
        });
        var flags = {};
        return this.categories.filter(function(entry) {
            if (flags[entry.title]) {
                return false;
            }
            flags[entry.title] = true;
            return true;
        });

    },

    filtered_items: function (val) {
      var set_selected_categories = new Set(this.selected_categories)
      console.log(set_selected_categories.size)
      if (set_selected_categories.size == 0)
        return this.resp
      else {
        
        return this.resp.filter(function(entry) {
          return set_selected_categories.has(entry.category.code)
          
      });

      }
    
    },
    search_url: function (val) {
      return this.url + 'search/1?q='
    },
    suggest_url: function (val) {
      return this.url + 'suggest/1?q='
    },
  },

  watch: {
    msg: function (val) {
      this.$axios
      .get(this.search_url+ this.msg)
      .then(response => (this.resp = response.data));
      this.$axios
      .get(this.suggest_url+ this.msg)
      .then(response => (this.sugg = response.data));
    },
    
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
