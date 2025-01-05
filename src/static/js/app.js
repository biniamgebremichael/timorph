

var myApp = angular.module('myApp',[]);

myApp.service('dataService', function($http) {
    this.getData = function(tense, word, callbackFunc) {
        $http({
            method: 'GET',
            url: "/"+tense+"/"+word
        }).then(function(data){
            callbackFunc(data);
        }) ;
     }
});

myApp.controller('generateCtrl', function($scope, dataService) {
    $scope.data = [];
    $scope.records = [
            "Alfreds Futterkiste",
            "Berglunds snabbköp",
            "Centro comercial Moctezuma",
            "Ernst Handel",
        ]
    $scope.tense="PAST";
    $scope.word="ነገረ";
    $scope.refresh = function() {
        dataService.getData($scope.tense, $scope.word, function(dataResponse) {
            $scope.data = dataResponse.data;
            console.log($scope.data)
        });
    }
    $scope.refresh();
});

