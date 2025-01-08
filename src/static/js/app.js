

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
    $scope.nounexample=["ዕድመ","መስተ","ድሙ","ኣሃዱ","ደቂ","ወለዲ","መኪና","ሬሳ","ግዜ","ውሳኔ","ቤት","ግቡእ","ኣቦ","ማዕጾ"]
    $scope.action = "refresh";
    $scope.records = [
            "Alfreds Futterkiste",
            "Berglunds snabbköp",
            "Centro comercial Moctezuma",
            "Ernst Handel",
        ]
    $scope.tense="PAST";
    $scope.word="ገደፈ";

    $scope.newword = function(nword) {
     $scope.word=nword;
    }
    $scope.refresh = function(tense,word) {
        $scope.tense=tense;
        $scope.word=word;
        $scope.action = "loading "+ word +"... please wait";
        dataService.getData($scope.tense, $scope.word, function(dataResponse) {
            $scope.data.push(dataResponse.data);
//            console.log($scope.data)
            $scope.action = "refresh";
        });
    }
});

