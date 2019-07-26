'use strict';
//window.jQuery = require('jquery');

//var Vue = require('vue');
// https://github.com/nuxt/nuxt.js/issues/1142
//window.Vue = require('vue/dist/vue.common');
//var Vue = require('vue/dist/vue.common');
window.Vue = require('vue/dist/vue.common');

var test = require('./test')

//window.onload = function(){
window.addEventListener('load', function(){

	//jQuery('.level-two').removeClass('is-hidden');

	console.log('test');
	console.log(test);

	window.browse_menu_items = new Vue( {
		el: '#browse-level-two',
		data: {
			isHidden: true,
			menu_selected: window.menu_selected
		},
		methods: {
			toggleVisibility : function(e) {
				e.preventDefault();
				if (this.isHidden == true) {
					this.isHidden = false;
				}

				else  {
					this.isHidden = true;
				}
			}

		}

	});

});