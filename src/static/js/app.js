
        function toggleSidebar() {
            document.getElementById("sidebar").classList.toggle("collapsed");
        }


var myApp = angular.module('myApp',[]);
myApp.filter('unique', function() {

  return function (arr, field) {
    var o = {}, i, l = arr.length, r = [];
    for(i=0; i<l;i+=1) {
      o[arr[i][field]] = arr[i];
    }
    for(i in o) {
      r.push(o[i]);
    }
    return r;
  };
})
myApp.service('dataService', function($http) {
    this.getData = function(tense, word, callbackFunc) {
        $http({
            method: 'GET',
            url: "/"+tense+"/"+word
        }).then(function(data){
            callbackFunc(data);
        }) ;
     };
    this.getUrl = function(url, callbackFunc) {
        $http({
            method: 'GET',
            url:url
        }).then(function(data){
            callbackFunc(data);
        }) ;
     };
});

myApp.controller('generateCtrl', function($scope, dataService) {
    $scope.data = [];
    $scope.parents = [  ];
    $scope.parentLimit = 0;
    $scope.myfeature = '';
    $scope.germinates = []
    $scope.nounexample=["ዕድመ","መስተ","ድሙ","ኣሃዱ","ደቂ","ወለዲ","ከልቢ","መዓልቲ","መኪና","ሬሳ","ግዜ","ውሳኔ","ቤት","መጽሓፍ","ፈረስ","ከረን","ኣቦ","ማዕጾ"]
    $scope.action = "refresh";
    $scope.tense="PAST";
    $scope.word="ረኸበ";

    $scope.newword = function(nword) {
     $scope.word=nword;
    }


    $scope.newfeature = function(feature) {
     $scope.myfeature=feature;
    }

    $scope.getParents = function(  ) {
    $scope.action = "loading";
     dataService.getUrl("/parents/"+$scope.parentLimit, function(dataResponse) {
                    $scope.parents = dataResponse.data ;
                    if($scope.parents.N.length <50 && $scope.parents.V.length <50 ){
                        $scope.parentLimit =  0;
                    }else{
                        $scope.parentLimit =  $scope.parentLimit+ 50;
                     }
                    $scope.action = "next " + ($scope.parentLimit );
                });
    };


    $scope.getGermination = function(pos,word ) {
    $scope.word=word;
     dataService.getUrl("/germinate/"+pos+"/"+word, function(dataResponse) {
                    $scope.germinates = dataResponse.data ;
                });
    };

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

