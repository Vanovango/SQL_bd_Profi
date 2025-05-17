import case1_create_db
import case1_add_data
import case1_create_backup

import case2__1_4
import case2_5
import case2__6_10


def main():
    case1_create_db.create_db()
    case1_add_data.main()
    # case1_create_backup.main()

    case2__1_4.load_all_data()
    case2_5.main()
    # case2__6_10.main()


if __name__ == "__main__":
    main()
