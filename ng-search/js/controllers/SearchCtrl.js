
angular.module('martisearch')
	.controller('SearchCtrl', function SearchCtrl($scope) {
		'use strict';

		var cont = angular.element( document.querySelector( '#container' ) );

		$scope.twttr = (function (d, s, id) {
			  var t, js, fjs = d.getElementsByTagName(s)[0];
			  if (d.getElementById(id)) return;
			  js = d.createElement(s); js.id = id;
			  js.src= "https://platform.twitter.com/widgets.js";
			  fjs.parentNode.insertBefore(js, fjs);
			  return window.twttr || (t = { _e: [], ready: function (f) { t._e.push(f) } });
			}(document, "script", "twitter-wjs"));


		$scope.twttr.widgets.createTweet(
		  '20',
		  document.getElementById('container'),
		  {
		    theme: 'dark'
		  }
		);

		// $scope.$watch('todos', function (newValue, oldValue) {
		// 	$scope.remainingCount = $filter('filter')(todos, { completed: false }).length;
		// 	$scope.completedCount = todos.length - $scope.remainingCount;
		// 	$scope.allChecked = !$scope.remainingCount;
		// 	if (newValue !== oldValue) { // This prevents unneeded calls to the local storage
		// 		todoStorage.put(todos);
		// 	}
		// }, true);

		// Monitor the current route for changes and adjust the filter accordingly.
		// $scope.$on('$routeChangeSuccess', function () {
		// 	var status = $scope.status = $routeParams.status || '';

		// 	$scope.statusFilter = (status === 'active') ?
		// 		{ completed: false } : (status === 'completed') ?
		// 		{ completed: true } : null;
		// });

	});