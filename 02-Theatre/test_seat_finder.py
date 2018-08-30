import unittest

from seat_finder import SeatFinder

#Test works as documentation what to need to implement

class SeatFinderTest(unittest.TestCase):

    @unittest.skip("WIP")
    def test_prefer_near_the_front(self):
        finder = SeatFinder(available_seats = {"A6", "B6", "C7"})
        seats = finder.find_seats(1)
        assert seats == {"A6"}

    @unittest.expectedFailure
    def test_finds_adjecent_seats_when_more_than_one_requested(self):
        finder = SeatFinder(available_seats = {"A6", "A8", "C6", "C7"})
        seats = finder.find_seats(2)
        assert seats == {"C6", "C7"}

    @unittest.expectedFailure
    def test_finds_separate_seats_when_adjecent_not_avalable(self):
        finder = SeatFinder(available_seats = {"A6", "B6", "C7"})
        seats = finder.find_seats(2)
        assert seats == {"B6", "A6"}

    @unittest.expectedFailure
    def test_find_seats_fails_when_not_enough_available(self):
        finder = SeatFinder(available_seats = {"A6", "B6", "C7"})
        seats = finder.find_seats(5)
        assert seats == {}

    @unittest.expectedFailure
    def test_find_seats_for_wheelchair_users_on_front_row(self):
        finder = SeatFinder(available_seats = {"A1W", "A6", "A7", "C7"})
        seats = finder.find_seats(1, wheelchair_count=1)
        assert seats == {"A1W"}

    
        














