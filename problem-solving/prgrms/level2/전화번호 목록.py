def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        std = phone_book[i]
        if std == phone_book[i + 1][0 : len(std)]:
            return False
    return True

def solution2(phone_book):
  phones = set(phone_book)
  for phone in phone_book:
    head = ""
    for num in phone:
      head += num
      if head in phones and head != phone:
        return False
  return True