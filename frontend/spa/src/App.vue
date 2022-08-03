<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@import'~bootstrap/dist/css/bootstrap.css';
@import './assets/css/styles.min.css'
.product-item{padding:10px}
.product-item .product-container{text-align:left;font:14px sans-serif;background-color:#fff;border:1px solid #dbe3e7;border-radius:3px;box-shadow:1px 3px 1px rgba(0,0,0,.08);padding:25px}.product-item a.product-image{display:block;text-align:center;box-shadow:0 0 20px 8px #f3f3f3 inset;width:100%;margin-bottom:25px;padding:20px 0;box-sizing:border-box}.product-item a.product-image img{height:130px}.product-item h2{font-size:18px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:200px;font-weight:800}.product-item h2 a{text-decoration:none;color:#2b2b2b}.product-item a.small-text{color:grey;text-decoration:none;margin-top:20px;margin-bottom:10px;display:block;text-align:right;font-size:12px}.product-item .product-rating{color:#f09911;font-size:14px}.product-item .product-rating a.small-text{text-align:left;margin:0 0 0 10px;display:inline-block}.product-item p.product-description{margin-top:20px;color:#5d5d5d;line-height:1.45;white-space:normal;margin-bottom:20px}.product-item button{border-radius:2px;background:#87bae1;box-shadow:0 1px 1px rgba(0,0,0,.12);border:0;color:#fff;font-weight:700;font-size:13px;padding:8px 20px}.product-item button:active{background:#87bae1;color:#fff;border:0}.product-item button:focus,.product-item button:focus:active{background:#87bae1;outline:0;color:#fff}.product-item button:hover{background:#66abe0;color:#fff}.product-item .product-price{color:#4e4e4e;font-weight:700;font-size:20px;padding-top:5px;text-align:right}.search-form{margin:40px 5px;font:12px sans-serif;box-shadow:1px 2px 4px 0 rgba(0,0,0,.08)}.search-form div.input-group-addon{background:#fff;color:#80a3bd;border-bottom-left-radius:2px;border-top-left-radius:2px;border:1px solid #b6c3cd;border-right:0}.search-form .input-group input{background-color:#fff;box-shadow:none;color:#4e565c;outline:0;border:1px solid #b6c3cd;border-right:0;border-left:0}.search-form div.input-group-btn button{border-bottom-right-radius:2px;border-top-right-radius:2px;background:#6caee0;box-shadow:1px 2px 4px 0 rgba(0,0,0,.08);color:#fff;border-color:#6caee0;outline:0;opacity:.9}.search-form div.input-group-btn button:hover{opacity:1}
.search-form div.input-group-btn button:focus:active{background-color:#6caee0;color:#fff;outline:0}
.o_heading{color:#4e565c;font-size:2em}
</style>
