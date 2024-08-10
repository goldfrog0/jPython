#!/usr/bin/env python3

class Connection:
    def __init__(self, connection_type: str, cost: float()) -> None:
        print(f'Connection Type: {connection_type} established! (Cost: ${cost}/h)')
        self.connection_type = connection_type
        self.cost = cost

    def close_connection(self) -> None:
        print(f'Closing {self.connection_type} connection...')


def main() -> None:
    internet: Connection = Connection("Internet", 2)
    satelite: Connection = Connection("Satelite", 20)

    internet.close_connection()
    satelite.close_connection()

if __name__ == "__main__":
    main()
