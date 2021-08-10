     /// <summary>
        /// this func. can be use when we got user comment in app and we want to clear extra space in the comment
        /// </summary>
        /// <param name="sentence">string that contain extra   space</param>
        /// <returns>returns a string with cleared extra space</returns>
        public static string ClearSentence(String sentence)
        {
            sentence = sentence.Trim();
            string recall = "";
            string space = " ";
            string temp;

           for(int i=0;i<sentence.Length;i++)
            {
                temp = sentence[i].ToString();
                if (temp !=space )
                {
                    if ( i != (sentence.Length - 1) && sentence[i + 1].ToString().Equals(space))
                    {
                        recall += sentence[i] + space;
                    }
                    else
                    {
                        recall += sentence[i];
                    }
                }
            }
            return recall;

        }