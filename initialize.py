# Copyright (c) Anish Athalye (me@anishathalye.com)
#
# This software is released under AGPLv3. See the included LICENSE.txt for
# details.

if __name__ == '__main__':
    from hammer.models import db
    db.create_all()
