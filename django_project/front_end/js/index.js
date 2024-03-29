/*! OHG v2.0.0 | (c) 2023 Your Name | MIT License | http://github.com/cferdinandi/build-tools-boilerplate */
(function () {
	'use strict';

	//window.jQuery = require('jquery');

	//var Vue = require('vue');
	// https://github.com/nuxt/nuxt.js/issues/1142
	//window.Vue = require('vue/dist/vue.common');
	//var Vue = require('vue/dist/vue.common');

	var Vue = require('vue/dist/vue.common'); 
	window.current_transcript = {
		"text": ""
	};

	Vue.component('recording', {
			props: ['transcript', 'transcript_document', 'file', 'extension'],
			//data: function() {  },
			methods: {
				show_transcript: function(event) { 
					event.preventDefault();
					console.log('test the transcript'); 
					console.log(this.transcript); 
					window.current_transcript.text = this.transcript;
				} 
			},
			template: 
				'<div class="recording_details">' +
				'<audio v-if="file" :src="file" controls="">Your browser does not support the audio element.</audio> ' +
				'<div v-if="file" class="recording-list__recording-download"><a :href="file">{{ extension }}</a></div> ' + 
				'<a v-if="transcript_document" :href="transcript_document" target="_blank">PDF</a> ' +
				'<a v-if="transcript" href="#" v-on:click="show_transcript">Transcript</a> ' +
				'</div>' 
	});

	// On document load
	window.addEventListener('load', function(){ 

		// Menu
		var browse_menu_items = new Vue( {
			el: '#browse-level-two',
			data: {
				notHidden: false,
				menu_selected: window.menu_selected
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
					else {
						return false;
					}

				}

			},
			mounted: function(){
				this.$nextTick(function(){
					if( this.checkIfNameOrSubject() ){
						this.notHidden = true;
					}
				});

			}

		});


		// Recordings on Name detail
		var recording_list = new Vue( 
			{
			el : '#recording-list',
			data: {
				recordings: window.recordings
			},
			template: '<div class="recordings">' +
			'<recording v-for="r in recordings" ' + 
				'v-bind:transcript="r.transcript" ' + 
				'v-bind:transcript_document =  "r.transcript_document" ' +
				'v-bind:file = "r.file" ' +
				'v-bind:extension = "r.extension" ' +
				'v-bind:key = "r.id" ' +
			'> </recording>' +
			'</div>'
			} 
		);

		// Transcript text from recording inline on Name detail page
		window.inline_transcript = new Vue({
			el: '#transcript_text',
			data: window.current_transcript ,
			template: 
				'<div class="transcript">' +
					'<div class="transcript__text" v-html="text">' +
					'</div>' +
				'</div>'
		});

	});

}());
