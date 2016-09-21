(function() {
    'use strict';

    angular
        .module('leaderboard')
        .factory('leaderboardService', leaderboardService);

    leaderboardService.$inject = ['$http'];

    function leaderboardService($http) {
        var apiUrl = 'http://psc.cpsc.ucalgary.ca/ranking.php';

        return {
            get: get
        };

        function get() {
            return $http.get(apiUrl)
                .then(function (response) {
                    return response.data;
                });
        }
    }
})();
