<template>
  <div class="search"> 
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet"/>
    <div class="container">
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
                <li class="ref-category" v-for="category in u_categories" :key="category.id" >
                <input type="checkbox"  :id="category.code" :ue="category.code" v-model="selected_categories"/>
                <span>{{category.title}}</span></li>
            </ul>
        </div>
    </div>
</div><div class="col-md-10">
    <p class="o_heading">Search results</p>
    <div class="row product-list">

        <div class="col-sm-6 col-md-4 product-item" v-for="item in filtered_items" :key="item.id">
            <a :href="item.link" class = 'item_link'>
            <div class="card mb-3" style="max-width: 540px;">
              <div class="row g-0">
                <div class="col-md-4">
                  <img :src="item.image_link" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title">{{item.title}}</h5>
                    <p class="card-text"></p>
                    <p class="card-text"><small class="text-muted">{{item.price}} {{item.currency_code}}</small></p>
                  </div>
                </div>
              </div>
            </div>
            </a>

        </div>
    </div>
</div></div>
    </div></div>
  
</template>

<script>
export default {
  name: 'HelloWorld',
  props:['hub_id'],
  data () {
    return {
      url: 'http://84.252.129.108:8000/',
      msg: '',
      sugg:{
        suggest:''
      },
      resp: [],
      selected_categories: [],
    }
  },
  computed:{
    categories: function () {
      var cat = [];
      this.resp.forEach(item => {
          cat.push(item.category)
        });
        return cat
    },
    u_categories: function () {
        var flags = {};
        return this.categories.filter(function(entry) {
            if (flags[entry.code]) {
                return false;
            }
            flags[entry.code] = true;
            return true;
        });

    },
    filtered_items: function () {
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
    search_url: function () {
      return this.url + 'search/'+this.hub_id+'?q='
    },
    suggest_url: function () {
      return this.url + 'suggest/'+this.hub_id+'?q='
    },
    randint() {
            return Math.random()
        },
  },

  watch: {
    msg: function () {
      fetch(this.search_url+ this.msg)
      .then(response => response.json())
      .then(data => (this.resp = data));
      fetch(this.suggest_url+ this.msg)
      .then(response => response.json())
      .then(data => (this.sugg = data));
    },
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search > .container{
  position: fixed;
  width: 100%;
  height: 100%;
  overflow:auto;
}
.img-fluid {
  width:100%;
  max-height: 10ch;
}
.item_link {
  opacity: 1;
}
.item_link:hover {
  opacity: 0.75;
}
.product-item{padding:10px; height:20ch;padding-top: 0;}
.product-item .product-container{text-align:left;font:14px sans-serif;background-color:#fff;border:1px solid #dbe3e7;border-radius:3px;box-shadow:1px 3px 1px rgba(0,0,0,.08);padding:25px}.product-item a.product-image{display:block;text-align:center;box-shadow:0 0 20px 8px #f3f3f3 inset;width:100%;margin-bottom:25px;padding:20px 0;box-sizing:border-box}.product-item a.product-image img{height:130px}.product-item h2{font-size:18px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:200px;font-weight:800}.product-item h2 a{text-decoration:none;color:#2b2b2b}.product-item a.small-text{color:grey;text-decoration:none;margin-top:20px;margin-bottom:10px;display:block;text-align:right;font-size:12px}.product-item .product-rating{color:#f09911;font-size:14px}.product-item .product-rating a.small-text{text-align:left;margin:0 0 0 10px;display:inline-block}.product-item p.product-description{margin-top:20px;color:#5d5d5d;line-height:1.45;white-space:normal;margin-bottom:20px}.product-item button{border-radius:2px;background:#87bae1;box-shadow:0 1px 1px rgba(0,0,0,.12);border:0;color:#fff;font-weight:700;font-size:13px;padding:8px 20px}.product-item button:active{background:#87bae1;color:#fff;border:0}.product-item button:focus,.product-item button:focus:active{background:#87bae1;outline:0;color:#fff}.product-item button:hover{background:#66abe0;color:#fff}.product-item .product-price{color:#4e4e4e;font-weight:700;font-size:20px;padding-top:5px;text-align:right}.search-form{margin:40px 5px;font:12px sans-serif;box-shadow:1px 2px 4px 0 rgba(0,0,0,.08)}.search-form div.input-group-addon{background:#fff;color:#80a3bd;border-bottom-left-radius:2px;border-top-left-radius:2px;border:1px solid #b6c3cd;border-right:0}.search-form .input-group input{background-color:#fff;box-shadow:none;color:#4e565c;outline:0;border:1px solid #b6c3cd;border-right:0;border-left:0}.search-form div.input-group-btn button{border-bottom-right-radius:2px;border-top-right-radius:2px;background:#6caee0;box-shadow:1px 2px 4px 0 rgba(0,0,0,.08);color:#fff;border-color:#6caee0;outline:0;opacity:.9}.search-form div.input-group-btn button:hover{opacity:1}
.search-form div.input-group-btn button:focus:active{background-color:#6caee0;color:#fff;outline:0}
.o_heading{color:#4e565c;font-size:2em}
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
