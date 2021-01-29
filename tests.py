import unittest

from main import gen_hashtags
from main import report


class GenHashtags(unittest.TestCase):
    """
        Tests that it can generate valid hashtags
    """
    def test_single_name(self):
        """ Simple test with an artist with only a name """ 
        result = gen_hashtags("BLACKPINK")
        self.assertEqual(result, "#music #youtube #stats #blackpink")

    def test_double_name(self):
        """ Test with an artist with name and surname """
        result = gen_hashtags("Dua Lipa")
        self.assertEqual(result, "#music #youtube #stats #dualipa #dua #lipa")

    def test_numeric_name(self):
        """ Test with an artist which name contains a number """
        result = gen_hashtags("Maroon 5")
        self.assertEqual(result, "#music #youtube #stats #maroon5 #maroon")

class Report(unittest.TestCase):
    """
        Tests that it can generate valid weekly reports
    """
    def test_report_truncated(self):
        """ Generate a report from a long list of channels (it will be truncated at 260 chars to respect max Tweet length) """ 
        channels = [{'name': 'Justin Bieber', 'username': 'justinbieber', 'id': 'UCIwFjwMjI0y7PDBVEO9-bkQ', 'subs': '60600000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjikPqZQLCLO0Dpiekl_ZkNcSB-1HMCy1Rz_f2UiA=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'BLACKPINK', 'username': 'BLACKPINK', 'id': 'UCOmHUn--16B90oW2L6FRR3A', 'subs': '56500000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjEDJWYaIksia0vpqmF1_jPxZz4oYeNnPG6zs-IBw=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Marshmello', 'username': 'marshmellomusic', 'id': 'UCEdvpU2pFRCVqU6yIPyTpMQ', 'subs': '51200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjZsVIxgLup9lFku3uKwv8WfPeUOmiRdjdJNidS4g=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Ed Sheeran', 'username': 'edsheeran', 'id': 'UC0C-w0YjGpqDXGB8IHb662A', 'subs': '46700000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnj8RtKKAlRthZGyfivC3fsPuYjXW_E0n6P3RoNj=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Ariana Grande', 'username': 'ArianaGrande', 'id': 'UC9CoOnJkIBMdeijd9qYoT_g', 'subs': '46600000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwngICx3BtKy8ZhsJUl37xoYPeaWWtZ3qXTVWG6gvug=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Eminem', 'username': 'Eminem', 'id': 'UCfM3zsQsOnfWNUppiycmBuw', 'subs': '46200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwngM9X_zqKIWwJ36gNEMIuY9-x3R9iRZ0RNS3dGlMQ=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'BTS', 'username': 'bts_bighit', 'id': 'UCLkAepWjdylmXSltofFvsYQ', 'subs': '44200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjy4eVbbuGAL8aXp_FuZawSr9FtJIpZnl4skL230g=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Taylor Swift', 'username': 'taylorswift13', 'id': 'UCqECaJ8Gagnn7YCbPEzWH6g', 'subs': '41200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhNORMY-JuggrilsyPBCJL7YI_KcpiAQyQOeEKyGa0=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Katy Perry', 'username': 'katyperry', 'id': 'UCYvmuw-JtVrTZQ-7Y4kd63Q', 'subs': '39600000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjOBYcsHLgLP-oNIr72n6hnrpHStgSQpk9NZ7-8qQ=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Billie Eilish', 'username': 'billieeilish', 'id': 'UCiGm_E4ZwYSHV3bcW1pnSeQ', 'subs': '38300000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhK0ws-dDeKz8k5ZJ6k0KAn_3RxrdwU3vB1ZpDGEw=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Alan Walker', 'username': 'IAmAlanWalker', 'id': 'UCJrOtniJ0-NWz37R30urifQ', 'subs': '38200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjsfDHGvv6gR8hvxLhCFyekPe1PK1DyFX4BU1WBOA=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Rihanna', 'username': 'rihanna', 'id': 'UCcgqSM4YEo5vVQpqwN-MaNw', 'subs': '36300000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnh1sZ8Y0mGlhOcdNor1ic3mn4NtTZsA6szvWSBKFw=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'One Direction', 'username': 'onedirection', 'id': 'UCb2HGwORFBo94DmRx4oLzow', 'subs': '34800000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnheYryR8utfH8g90GmCG_41iKKq3b9MsV4xQpZtYAI=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Maroon 5', 'username': 'maroon5', 'id': 'UCBVjMGOIkavEAhyqpxJ73Dw', 'subs': '33100000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhtPNkQphmOSVeJD-s0L5Ap1YyVSfw8hrNTlv0vaA=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Daddy Yankee', 'username': 'daddy_yankee', 'id': 'UC9TO_oo4c_LrOiKNaY6aysA', 'subs': '32700000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhuOyDarXBY84x0k8asaRPVeMy5rhFnErspYpCN5g=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Ozuna', 'username': 'ozuna', 'id': 'UCjIA3wwhi0QjSOXAZwOXbPA', 'subs': '32200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwng2mp1cj4vUWR1Tr3I6jtAbjk9LOR9jFXSAslgG6Q=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Shakira', 'username': 'shakira', 'id': 'UCYLNGLIzMhRTi6ZOLjAPSmw', 'subs': '31900000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhO7sMbG8HGnK4iHvo59QrujJ5d3cUNLKKU8H-WfSU=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Bad Bunny', 'username': 'sanbenito', 'id': 'UCmBA_wu8xGg1OfOkfW13Q0Q', 'subs': '31500000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjSMssRx-Oeo-hpnM6hSyadbrKcvH_OTr3GbN94sQ=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'J Balvin', 'username': 'jbalvin', 'id': 'UCt-k6JwNWHMXDBGm9IYHdsg', 'subs': '30000000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnhu9VAVKjomWYLoTEZ8JeAyotQ3VDH2WWztYDt1XQ=s240-c-k-c0x00ffffff-no-rj-mo'}]
        expected_result = "Weekly report top #youtube #music channels\n@justinbieber 60.6 Mln\n@BLACKPINK 56.5 Mln\n@marshmellomusic 51.2 Mln\n@edsheeran 46.7 Mln\n@ArianaGrande 46.6 Mln\n@Eminem 46.2 Mln\n@bts_bighit 44.2 Mln\n@taylorswift13 41.2 Mln\n@katyperry 39.6 Mln\n@billieeilish 38.3 Mln"
        
        result = report(channels)
        self.assertEqual(result, expected_result)

    def test_report_not_truncated(self):
        """ Generate a report from a shor list of channels (it won't be truncated) """ 
        channels = [{'name': 'Justin Bieber', 'username': 'justinbieber', 'id': 'UCIwFjwMjI0y7PDBVEO9-bkQ', 'subs': '60600000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjikPqZQLCLO0Dpiekl_ZkNcSB-1HMCy1Rz_f2UiA=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'BLACKPINK', 'username': 'BLACKPINK', 'id': 'UCOmHUn--16B90oW2L6FRR3A', 'subs': '56500000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjEDJWYaIksia0vpqmF1_jPxZz4oYeNnPG6zs-IBw=s240-c-k-c0x00ffffff-no-rj-mo'}, {'name': 'Marshmello', 'username': 'marshmellomusic', 'id': 'UCEdvpU2pFRCVqU6yIPyTpMQ', 'subs': '51200000', 'img': 'https://yt3.ggpht.com/ytc/AAUvwnjZsVIxgLup9lFku3uKwv8WfPeUOmiRdjdJNidS4g=s240-c-k-c0x00ffffff-no-rj-mo'}]
        expected_result = "Weekly report top #youtube #music channels\n@justinbieber 60.6 Mln\n@BLACKPINK 56.5 Mln\n@marshmellomusic 51.2 Mln"
        
        result = report(channels)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()