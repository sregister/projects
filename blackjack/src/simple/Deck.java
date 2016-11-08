package simple;

import java.util.Random;

public class Deck {
	public Card[] d;

	public Deck() {
		d = new Card[52];
		String[] suits = { "\u2661", "\u2667", "\u2662", "\u2664" };

		for (int i = 0; i < 52; ++i) {

			// set suits
			if (i < 13) {
				d[i] = new Card(Integer.toString(i + 1), suits[0]);
			} else if (i >= 13 && i < 26) {
				d[i] = new Card(Integer.toString(i - 12), suits[1]);
			} else if (i >= 26 && i < 39) {
				d[i] = new Card(Integer.toString(i - 25), suits[2]);
			} else if (i >= 39 && i < 52) {
				d[i] = new Card(Integer.toString(i - 38), suits[3]);
			}

			// Set face cards
			if (d[i].getVal().equals("1")) {
				d[i].setVal("Ace");
			}
			if (d[i].getVal().equals("11")) {
				d[i].setVal("Jack");
			}
			if (d[i].getVal().equals("12")) {
				d[i].setVal("Queen");
			}
			if (d[i].getVal().equals("13")) {
				d[i].setVal("King");
			}
		}

	}

	// Algorithm: Fisher-Yates: finite set shuffle
	public void shuffle() {
		int index;
		Card temp;
		Random random = new Random();
		for (int i = d.length - 1; i > 0; i--) {
			index = random.nextInt(i + 1);
			temp = d[index];
			d[index] = d[i];
			d[i] = temp;
		}

	}

	public void printDeck() {
		for (Card c : this.d) {
			c.printCard();
			System.out.println();
		}
	}

}
