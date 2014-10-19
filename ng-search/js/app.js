angular.module('martisearch', ['ngRoute'])
	.config(function ($routeProvider) {
		'use strict';

		$routeProvider.when('/', {
			controller: 'SearchCtrl',
			templateUrl: 'search-index.html'
		}).otherwise({
			redirectTo: '/'
		});
	});