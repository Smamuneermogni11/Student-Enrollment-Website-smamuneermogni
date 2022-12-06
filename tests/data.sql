INSERT INTO user (
                     email,
                     password,
                     name,
                     dep_id,
                     rol_id
                 )
                 VALUES (
                     'Test@test.com',
                     'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f',
                     'TestUser',
                     '1',
                     '2'
                 );
INSERT INTO loc (
                    loc_Cap,
                    loc_name
                )
                VALUES (
                    '65',
                    'TesT Room'
                );