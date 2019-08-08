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
			notHidden: false,
			menu_selected: window.menu_selected,
			message: ''
		},
		methods: {
			toggleVisibility : function(e) {
				e.preventDefault();
				if (this.notHidden == true) {
					this.notHidden = false;
				}

				else  {
					this.notHidden = true;
				}
			},
			checkIfNameOrSubject: function(){
				if (window.menu_selected === 'names'){
					return true;
				}
				else if(window.menu_selected === 'subjects'){
					return true;
				}
				else{
					return false;
				}

			}

		},
		mounted: function(){
			this.$nextTick(function(){
				if( this.checkIfNameOrSubject() ){
					this.notHidden = true;
				}
			})

		}

	});

});