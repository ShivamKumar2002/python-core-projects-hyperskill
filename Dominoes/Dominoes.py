import random

# Allowed numbers
numbers = range(0, 7)


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def generate_domino_set():
    new_domino_set = []
    while len(new_domino_set) != 28:
        # Generate a random piece
        domino_piece = [random.choice(numbers) for _ in range(2)]

        # Check if the piece with same numbers already exists
        if domino_piece in new_domino_set:
            continue
        domino_piece.reverse()
        if domino_piece in new_domino_set:
            continue

        # Add piece to set
        new_domino_set.append(domino_piece)
    return new_domino_set


# Outer Loop
while True:
    # Generate a domino set
    domino_set = generate_domino_set()

    # Define variables
    domino_snake = []
    status = ""
    is_draw = False

    # Shuffle the set before distributing pieces
    random.shuffle(domino_set)

    # Distribute pieces
    stock_pieces = domino_set[:14]
    computer_pieces = domino_set[14:21]
    player_pieces = domino_set[21:28]

    # Find double number pieces
    computer_doubles = [x for x in computer_pieces if x[0] == x[1]]
    player_doubles = [x for x in player_pieces if x[0] == x[1]]

    # Restart the game if no player has doubles
    if len(computer_doubles) == 0 and len(player_doubles) == 0:
        continue

    # Determine who will donate piece
    if len(computer_doubles) == 0:
        starter = "player"
    elif len(player_doubles) == 0:
        starter = "computer"
    else:
        if max(computer_doubles) > max(player_doubles):
            starter = "computer"
        else:
            starter = "player"

    # Make the first move - Add donated piece to domino snake and remove it from donor's pieces, then set next player
    if starter == "computer":
        donated_piece = max(computer_doubles)
        computer_pieces.remove(donated_piece)
        domino_snake.append(donated_piece)
        status = "player"
    else:
        donated_piece = max(player_pieces)
        player_pieces.remove(donated_piece)
        domino_snake.append(donated_piece)
        status = "computer"

    # Game Loop
    while True:
        # Print header
        print("=" * 70)

        # Print additional info
        print("Stock size:", len(stock_pieces))
        print("Computer pieces:", len(computer_pieces))
        print()

        # Print domino snake
        if len(domino_snake) <= 6:
            for piece in domino_snake:
                print(piece, end="")
        else:
            for i in range(3):
                print(domino_snake[i], end="")
            print("...", end="")
            for i in range(len(domino_snake) - 3, len(domino_snake)):
                print(domino_snake[i], end="")
        print("\n")

        # Print player's pieces
        print("Your pieces:")
        for i in range(len(player_pieces)):
            print(str(i + 1) + ":" + str(player_pieces[i]))
        print()

        # Check if game over
        if len(player_pieces) == 0:
            print("Status: The game is over. You won!")
            break
        if len(computer_pieces) == 0:
            print("Status: The game is over. The computer won!")
            break

        # Check condition of draw
        if domino_snake[0][0] == domino_snake[-1][1]:
            if str(domino_snake).count(str(domino_snake[0][0])) == 8:
                print("Status: The game is over. It's a draw!")
                break
        if is_draw:
            print("Status: The game is over. It's a draw!")
            break

        # Play next move
        if status == "computer":
            print("Status: Computer is about to make a move. Press Enter to continue...")
            input()

            # Prepare the list holding the count of each number occurence
            num_occurences = list()
            for i in range(7):
                num_occurences.append(str(computer_pieces).count(str(i)) + str(domino_snake).count(str(i)))

            # Calculate the scores of every domino piece in hand
            piece_scores = dict()
            for piece in computer_pieces:
                piece_scores[str(computer_pieces.index(piece))] = num_occurences[piece[0]] + num_occurences[piece[1]]

            invalid_move_right = False

            # Use AI to choose move
            while True:
                command = int(max(piece_scores, key=piece_scores.get))
                invalid_move_right = (int(command) > 0) and (domino_snake[-1][1] not in computer_pieces[abs(int(command)) - 1])
                invalid_move_left = (int(command) < 0) and (domino_snake[0][0] not in computer_pieces[abs(int(command)) - 1])
                full_invalid_move = invalid_move_left and invalid_move_right
                if not full_invalid_move:
                    break
                else:
                    del piece_scores[max(piece_scores, key=piece_scores.get)]
                    if len(piece_scores) == 0:
                        command = 0
                        break

            if invalid_move_right:
                command = -command
            command_giver = "computer"
            status = "player"

        else:
            print("Status: It's your turn to make a move. Enter your command.")
            command = input()
            invalid_input = not check_int(command) or int(command) not in range(-len(player_pieces), len(player_pieces) + 1)
            invalid_move = False

            # Check if move is invalid only if input is valid
            if not invalid_input:
                invalid_move = ((int(command) > 0) and (domino_snake[-1][1] not in player_pieces[abs(int(command)) - 1])) or ((int(command) < 0) and (domino_snake[0][0] not in player_pieces[abs(int(command)) - 1]))

            while invalid_input or invalid_move:
                if invalid_input:
                    print("Invalid input. Please try again.")
                elif invalid_move:
                    print("Illegal move. Please try again.")
                command = input()

                # Re-check if input is invalid
                invalid_input = not check_int(command) or int(command) not in range(-len(player_pieces), len(player_pieces) + 1)

                # Re-check new command to make sure move is valid
                if not invalid_input:
                    invalid_move = ((int(command) > 0) and (domino_snake[-1][1] not in player_pieces[abs(int(command)) - 1])) or ((int(command) < 0) and (domino_snake[0][0] not in player_pieces[abs(int(command)) - 1]))
            command_giver = "player"
            status = "computer"

        # Process command
        command = int(command)
        if command == 0:
            # Check if stock empty
            if len(stock_pieces) == 0:
                is_draw = True
                continue

            else:
                # Choose a piece from stock
                random_piece = random.choice(stock_pieces)

                # Give chosen piece to specified party
                if command_giver == "player":
                    player_pieces.append(random_piece)
                else:
                    computer_pieces.append(random_piece)

                # Remove chosen piece from stock
                stock_pieces.remove(random_piece)
            # Skip the move
            continue

        # Take specified piece and put on specified side of domino snake
        if command_giver == "player":
            selected_piece = player_pieces[abs(command) - 1]
        else:
            selected_piece = computer_pieces[abs(command) - 1]

        if command > 0:
            # Correct the piece orientation if needed
            if domino_snake[-1][1] == selected_piece[0]:
                pass
            else:
                selected_piece.reverse()
            # Add piece to domino snake
            domino_snake.append(selected_piece)
        else:
            # Correct the piece orientation if needed
            if domino_snake[0][0] == selected_piece[1]:
                pass
            else:
                selected_piece.reverse()
            domino_snake.insert(0, selected_piece)

        if command_giver == "player":
            player_pieces.remove(selected_piece)
        else:
            computer_pieces.remove(selected_piece)

    # Terminate outer loop so we don't get infinite loop
    break
