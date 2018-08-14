#!/usr/bin/env python

import psycopg2


def db_connect():
    """
    Creates and returns a db connection & cursor instance as a tuple: db, cur
    Returns: (db, cur)
    """

    db = psycopg2.connect("dbname=news")  # connect to news database
    cur = db.cursor()  # create cursor instance

    return db, cur


def execute_query(query):
    """
    Input: SQL query
    This function executes query and returns results as a list of tuples
    Returns: list of tuples containing the results of the query
    """

    db, c = db_connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_top_articles():
    """Prints out the top 3 articles of all time."""

    pop_3_query = "SELECT view_count, article_title FROM " \
                  "viewcount_article_author ORDER BY view_count DESC LIMIT 3;"
    results = execute_query(pop_3_query)

    print "\nThe most popular 3 articles of all time:\n"
    for views, title in results:
        print "{} views - {}".format(str(views), title)


def print_top_authors():
    """Prints a list of authors ordered by article views."""

    pop_authors_query = "SELECT author_name, sum(view_count) as total_views " \
                        "FROM viewcount_article_author GROUP BY author_name" \
                        " ORDER BY total_views DESC;"
    results = execute_query(pop_authors_query)

    print "\nThe most popular article authors of all time:\n"
    for author, views in results:
        print "{} views - {}".format(str(views), author)


def print_errors_over_one():
    """Prints out the date(s) where more than 1% of requests were errors."""

    date_error_rate_query = "SELECT status_date, ROUND(CAST(total_errors " \
                            "AS NUMERIC) / CAST(total_statuses AS NUMERIC) " \
                            "* 100, 2) AS error_rate FROM date_error_count;"
    results = execute_query(date_error_rate_query)

    print "\nDate(s) with error rate percentage greater than 1% of total " \
          "requests:"
    for date, rate in results:
        print "{} - {} percent".format(date, str(rate))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
    print ""
