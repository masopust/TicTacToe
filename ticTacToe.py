try:
    import TicTacToe.main as main
except FileNotFoundError:
    import main

if __name__ == "__main__":
    main.main()