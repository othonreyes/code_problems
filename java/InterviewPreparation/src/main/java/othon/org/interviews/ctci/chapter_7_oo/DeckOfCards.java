package othon.org.interviews.ctci.chapter_7_oo;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class DeckOfCards {
}

class Deck {
    List<Card> cards;

    public Deck() {
        cards = new ArrayList<>();
        init();
    }

    void shuffle(){
        // shuffle the cards
    }
    Card returnCardFromTop() {
        return cards.remove(cards.size() - 1);
    }
    void init() {
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j <= 13; j++) {
                switch (j) {
                    case 1:
                        cards.add(new Card(j, "As", CardType.values()[i]));
                        break;
                    case 11:
                        cards.add(new Card(j, "Joker", CardType.values()[i]));
                    break;
                    case 12:
                        cards.add(new Card(j, "Queen", CardType.values()[i]));
                        break;
                    case 13:
                        cards.add(new Card(j, "King", CardType.values()[i]));
                        break;
                    default:
                        cards.add(new Card(j, CardType.values()[i]));
                        break;
                }
            }
        }
    }
}

enum CardType {
    SPADEs, HEARTS, TREBOL, DIAMOND;
}

class Card {
    boolean faceUp;
    int value;
    String symbol;
    CardType type;

    public Card(int value, CardType type) {
        this(value, String.valueOf(value), type);
    }

    public Card(int value, String symbol, CardType type) {
        this.value = value;
        this.symbol = symbol;
        this.type = type;
    }

    void overrideValue(int v) {
        value = v;
    }

    Card faceUp() {
        this.faceUp = true;
        return this;
    }
}

enum ActionType {
    STAY, HIT;
}
interface BJPlayer extends  BJParticipant {
    void deposit (int moMoney);
    int bet();
    ActionType action();
    void settle();
    boolean isSettle();
}

class Player implements BJPlayer {
    List<Card> cards;
    int money;
    boolean settle;

    @Override
    public void receiveCard(Card card) {
        cards.add(card);
    }

    @Override
    public void deposit(int moMoney) {
        money += moMoney;
    }

    @Override
    public int bet() {
        return new Random().nextInt(money);
    }

    @Override
    public ActionType action() {
        if (evaluate()<=16) {
            return ActionType.HIT;
        }
        settle = true;
        return ActionType.STAY;
    }

    @Override
    public void settle() {
        settle = true;
    }

    @Override
    public boolean isSettle() {
        return settle;
    }

    @Override
    public int evaluate() {
        return cards.stream().mapToInt(c -> c.value).sum();
    }

}
interface BJParticipant {
    int evaluate();

    void receiveCard(Card card);
}
interface BJDealer extends BJParticipant {
    Card dealFaceUp(Deck deck);
    Card dealFaceDown(Deck deck);
}

class Dealer implements BJDealer {
    Deck deck;
    List<Card> cards;

    public Dealer(Deck deck) {
        this.deck = deck;
    }

    public Card dealFaceUp(Deck deck) {
        return deck.returnCardFromTop();
    }

    @Override
    public Card dealFaceDown(Deck deck) {
        return deck.returnCardFromTop().faceUp();
    }

    @Override
    public void receiveCard(Card card) {
        cards.add(card);
    }

    @Override
    public int evaluate() {
        return cards.stream().mapToInt(c -> c.value).sum();
    }
}


class BlackJack {
    Deck deck;
    BJDealer dealer;
    List<BJPlayer> players;
    Map<BJPlayer, Integer> bets;

    BlackJack(BJDealer dealer, List<BJPlayer> players) {
        deck = new Deck();
        this.dealer = dealer;
        this.players = players;
        bets = new HashMap<>();
    }

    void play() {
        deck.shuffle();
        // Beggining of the game
        for (BJPlayer p : players) {
            bets.put(p, p.bet());
        }
        deaclCardFaceUpToPlayers();
        dealer.receiveCard(dealer.dealFaceUp(deck));
        deaclCardFaceUpToPlayers();

        // Evaluate cards
        for (BJPlayer p : players) {
            if (21 == p.evaluate()) {
                int money = (int) (bets.get(p) * 1.5);
                p.deposit(money);
                p.settle();
            }
        }

        // Rounds
        boolean allPlayersNotSettle = false;
        while (!allPlayersNotSettle) {
            for (BJPlayer p : players) {
                ActionType action = p.action();
                if (ActionType.HIT.equals(action)) {
                    allPlayersNotSettle = false;
                    p.receiveCard(dealer.dealFaceUp(deck));
                }
            }
        }
        int dealersHand = dealer.evaluate();
        if (dealersHand == 21) {
            // collect bets
            return;
        }
        players.stream().filter(p -> !p.isSettle()).forEach(p->{
            int playerHand = p.evaluate();
            if (playerHand > dealersHand && playerHand < 22) {
                int money = bets.get(p) * 2;
                p.deposit(money);
            }
        });
    }

    private void deaclCardFaceUpToPlayers() {
        for (BJPlayer p : players) {
            p.receiveCard(dealer.dealFaceUp(deck));
        }
    }

}