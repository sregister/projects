package simple;

public class Card {
	public String value;
	public String suit;

	public Card() {
		value = "null";
		suit = "null";
	}

	public String CardToString() {
		return value + " " + suit;
	}

	public Card(String val, String s) {
		value = val;
		suit = s;
	}

	public void setCard(String val, String s) {
		value = val;
		suit = s;
	}

	public void printCard() {
		System.out.print(CardToString());
	}

	public String getVal() {
		return value;
	}

	public String getSuit() {
		return suit;
	}

	public void setVal(String s) {
		this.value = s;
	}

}
