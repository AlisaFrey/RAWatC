import copy
import logging
import math

# These are the AnonPay algorithms ROD, NUN and SPA.
# They must be invoked manually from within your app.
# Example: ../Game/models.py, set_and_adjust_payments.
# The remainder of this directory is the oTree equivalent of CPY+TDY.


def count(iterable, x):
    return sum(1 for el in iterable if el == x)


def has_unique_pi(paym):
    return any(count(paym, pi) == 1 for pi in paym)


def bayes(paym, attr, q):
    a = sum(1 for (i, el) in enumerate(paym) if el == q and attr[i] == 1)
    a /= count(attr, 1)

    b = sum(1 for (i, el) in enumerate(paym) if el == q and attr[i] == 0)
    b /= count(attr, 0)

    c = count(attr, 1)/len(paym)

    return (a * c)/(a * c + b * (1 - c))


def rod(paym, chi):
    return [math.ceil(pi/chi)*chi for pi in paym]


def nun(paym):
    paym = copy.deepcopy(paym)

    if len(paym) > 3:
        s = 1

        while True:
            if s == 1:
                rank = [sum(1 for pi2 in paym if pi2 >= pi) for pi in paym]

            if count(rank, s) > 0:
                q = [paym[i] for (i, r) in enumerate(rank) if r == s][0]

                if count(paym, q) == 1:
                    who1 = max((pi for pi in paym if pi < q),
                               default=-math.inf)
                    who2 = min((pi for pi in paym if pi > q),
                               default=+math.inf)

                    if (count(paym, who1) > 0 and
                            count(paym, who1)*(q-who1) <= who2-q):
                        for (i, pi) in enumerate(paym):
                            if pi == who1:
                                paym[i] = q

                                s = 0
                                break
                    else:
                        for (i, pi) in enumerate(paym):
                            if pi == q:
                                paym[i] = who2

            s = s + 1

            if s > len(paym):
                break

        return paym
    else:
        logging.warning('few subjects, payments all equalized')

        return [max(paym) for _ in paym]


def spa(paym, attr, eta):
    paym = copy.deepcopy(paym)

    if (1 > eta > 0 and
            len(paym) > 3 and
            count(attr, 1) > 0 and
            count(attr, 0) > 0):
        s = 1
        has_unique = has_unique_pi(paym)

        while True:
            if s == 1:
                rank = [sum([1 for pi2 in paym if pi2 >= pi]) for pi in paym]

            if count(rank, s) > 0:
                q = [paym[i] for (i, r) in enumerate(rank) if r == s][0]

                if count(attr, 1)/len(paym) > eta:
                    logging.error('too many attribute bearers, infeasible')

                    break
                else:
                    while bayes(paym, attr, q) > eta:
                        if (any(pi < q for (i, pi) in enumerate(paym) if attr[i] == 0) or
                                any(pi > q for (i, pi) in enumerate(paym) if attr[i] == 0)):
                            who1 = max((pi for (i, pi) in enumerate(paym) if pi < q and attr[i] == 0), default=-math.inf)
                            who2 = min((pi for (i, pi) in enumerate(paym) if pi > q and attr[i] == 0), default=+math.inf)

                            c = sum(1 for (i, pi) in enumerate(paym) if pi == who1 and attr[i] == 0)

                            if c > 0 and c*(q-who1) <= count(paym, q)*(who2-q):
                                for (i, pi) in enumerate(paym):
                                    if pi == who1 and attr[i] == 0:
                                        paym[i] = q
                                        break

                                s = 0
                                break
                            else:
                                for (i, pi) in enumerate(paym):
                                    if pi == q:
                                        paym[i] = who2

                                s = 0
                                break
                        else:
                            logging.error('ERROR: no valid candidates')  # should be impossible
                            break

                    if s == len(paym) and not has_unique:
                        if any(count(paym, pi) == 1 for pi in paym):
                            paym = nun(paym)
                            s = 0

            s = s + 1

            if s > len(paym):
                break
    elif eta <= 0 or eta >= 1:
        logging.error('invalid value for eta, must be between 0 and 1, SPA cannot run')
    elif len(paym) <= 3:
        logging.warning('few subjects, payments all equalized')

        return [max(paym) for _ in paym]
    elif count(attr, 1) != 0:
        logging.error('too few subjects, SPA cannot run')

    return paym
