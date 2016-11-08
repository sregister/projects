package simple;

import java.util.Scanner;
import java.util.Random;

public class Game {
	static Deck deck = new Deck();

	public int begin() {
		Card[] dealer = new Card[2];
		Card[] user = new Card[2];
		Boolean not_finished = true;
		Scanner kb = new Scanner(System.in);
		String response = new String();
		int userhand;
		int dealerhand;

		while (not_finished) {
			deck.shuffle();

			// Deal cards
			System.out.printf("\n****Dealing to dealer****\n");
			DealCards(dealer);
			System.out.printf("****Dealing to player****\n");
			DealCards(user);
			// dealer show a card
			System.out.printf("Dealer shows: %s\n", dealer[0].CardToString());
			System.out.printf("Player shows: %s, %s\n", user[0].CardToString(), user[1].CardToString());

			// ask user for input
			userhand = GetUserInput(user);

			// Dealer plays
			dealerhand = AiPlay(dealer);

			// unused
			GetWinner(userhand, dealerhand);

			System.out.printf("\nWould you like to play again? (y/n): ");
			response = kb.nextLine();
			if (response.equalsIgnoreCase("y") || response.equalsIgnoreCase("n")) {
				if (response.equalsIgnoreCase("y")) {
					continue;
				} else {
					System.out.printf("Goodbye...\n");
					not_finished = false;
					kb.close();
					return 0;
				}
			}

		}
		kb.close();
		return 0;

	}

	public static int AiPlay(Card[] player) {
		boolean playFinished = false;
		Integer[][] handValue = new Integer[12][2];
		int value;
		int handSize;

		System.out.printf("---> Dealer has %s, %s\n", player[0].CardToString(), player[1].CardToString());
		handValue[0] = CalculateValue(player[0]);
		handValue[1] = CalculateValue(player[1]);
		handSize = 2;
		value = handValue[0][0] + handValue[1][0];

		while (!playFinished) {
			System.out.printf("----> Value of hand: %d\n", value);
			if (value < 17) {
				// TODO: add ace as 1 edge case
				Card c = DealCard();
				System.out.printf("-----> Dealer Hits: %s\n", c.CardToString());
				handValue[handSize] = CalculateValue(c);
				value += handValue[handSize][0];
				handSize++;
			} else if (value > 21) {
				// dealer busts, go to end of game
				System.out.printf("----> Dealer busts!!!\n");
				playFinished = true;
				return value;
			} else {
				System.out.printf("----> Dealer stands\n");
				playFinished = true;
				return value;
			}

		}

		return -1;

	}

	public static int GetWinner(int user, int dealer) {
		// first check if user has bust
		System.out.printf("\n\nuser: %d \t dealer: %d\n", user, dealer);
		if (user > 21) {
			System.out.printf("****Player loses!****\n");
			return 0;
		} else if (dealer > 21) {
			System.out.printf("****Dealer loses!****\n");
			return 0;
		} else if (user == dealer) {
			System.out.printf("****Tie!****\n");
			return 0;
		} else if (user > dealer) {
			System.out.printf("****Player wins!****\n");
			return 0;
		} else {
			// should never be entered
			System.out.printf("**** error ****\n");
			return -1;
		}
	}

	public static Card DealCard() {
		Card c = new Card();
		Random random = new Random(System.currentTimeMillis());
		boolean valid_card = false;
		int index = 0;

		// deal first card
		while (!valid_card) {
			index = random.nextInt(52);

			// if card hasn't been dealt
			if (!deck.d[index].getSuit().equals("null")) {
				// clone the card and stop looking for a valid card
				c = new Card(deck.d[index].getVal(), deck.d[index].getSuit());
				valid_card = true;
			}
			// remove card from deck
			deck.d[index].setCard("null", "null");
		}
		return c;

	}

	public static int GetUserInput(Card[] player) {

		boolean playFinished = false;
		Scanner kb = new Scanner(System.in);
		String response = new String();
		Integer[][] handValue = new Integer[12][2];
		int value;
		int handSize;

		System.out.printf("---> Player has %s, %s\n", player[0].CardToString(), player[1].CardToString());
		handValue[0] = CalculateValue(player[0]);
		handValue[1] = CalculateValue(player[1]);
		handSize = 2;
		value = handValue[0][0] + handValue[1][0];
		System.out.printf("----> Value of: %d\n", value);

		while (!playFinished) {
			System.out.printf("----> Value of hand: %d\n", value);
			System.out.printf("Hit or stand? (h/s): ");
			response = kb.nextLine();
			if (response.equalsIgnoreCase("h")) {
				// TODO: add ace as 1 edge case
				Card c = DealCard();
				System.out.printf("-----> Hit: %s\n", c.CardToString());
				handValue[handSize] = CalculateValue(c);
				value += handValue[handSize][0];
				handSize++;
			}
			if (response.equalsIgnoreCase("s")) {
				System.out.printf("----> Player stands\n");
				playFinished = true;
				return value;
			}
			if (value > 21) {
				// player busts, go to end of game
				System.out.printf("----> Player busts!!!\n");
				playFinished = true;
				return value;
			}

		}
		return -1;
	}

	public static int DealCards(Card[] player) {
		// give the cards to player
		player[0] = DealCard();
		player[1] = DealCard();

		return 0;
	}

	private static Integer[] CalculateValue(Card c) {

		// format: val[0] = value, val[1] = 1 if is ace
		Integer[] val = new Integer[2];
		if (c.getVal().equals("King") || c.getVal().equals("Queen") || c.getVal().equals("Jack")) {
			val[0] = 10;
			val[1] = 0;
		} else if (c.getVal().equals("Ace")) {
			val[0] = 11;
			val[1] = 1;
		} else {
			val[0] = Integer.parseInt(c.getVal());
			val[1] = 0;
		}

		return val;

	}

}
