import case1_create_db
import case1_add_data
import case1_create_backup

import case2_1
import case2_2
import case2_3
import case2_4

def main():
    case1_create_db.create_db()
    case1_add_data.main()
    # case1_create_backup.main()

    case2_1.main()
    case2_2.main()
    case2_3.main()
    case2_4.main()


if __name__ == "__main__":
    main()
