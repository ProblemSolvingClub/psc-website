(function() {
    'use strict';

    angular
        .module('leaderboard')
        .controller('LeaderboardController', LeaderboardController);

    LeaderboardController.$inject = ['leaderboardService'];

    function LeaderboardController(leaderboardService) {
        var vm = this;
        vm.getUserDisplayName = getUserDisplayName;
        vm.getDisplayScore = getDisplayScore;
        vm.getTier = getTier;
        vm.users = [];
        vm.sites = [];
        vm.tiers = [];

        leaderboardService.get()
            .then(function(response) {
                console.log('Response:', response);
                vm.users = response.users.map(user => ({
                    ...user,
                    totalSolved: parseFloat(user.totalSolved),
                    attendedMeetings: parseInt(user.attendedMeetings, 10),
                    bonusProblems: parseInt(user.bonusProblems, 10)
                }));
                vm.sites = response.sites;
                vm.tiers = response.tiers;
            });

        function getUserDisplayName(user) {
            var displayName = user.firstName;
            if (user.lastName) {
                displayName += ' ' + user.lastName.charAt(0) + '.';
            }
            return displayName;
        }

        function getDisplayScore(score) {
            return score > 0 ? score.toFixed(2) : 0;
        }

        function getTier(totalSolved) {
            for (var i = vm.tiers.length - 1; i >= 0; i--) {
                console.log("I-Value: " + i);
                if (getDisplayScore(totalSolved) >= parseFloat(vm.tiers[i].minimumScore)) {
                    return vm.tiers[i];
                }
            }
        }
    }
})();
