import asyncio
from datetime import datetime
from typing import List


class TimestampGenerator:
    def generate_id(self) -> int:
        now = datetime.now()
        year = now.year % 100
        month_last_digit = int(str(now.month)[-1])
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        millisecond_first_two = int(now.microsecond / 10000)

        result = (
            f"{year:02}"
            f"{month_last_digit}"
            f"{day:02}"
            f"{hour:02}"
            f"{minute:02}"
            f"{second:02}"
            f"{millisecond_first_two:02}"
        )
        return int(result)

    async def generate_sequence(self, count: int) -> List[int]:
        sequence = []
        for i in range(count):
            await asyncio.sleep(0.0001)
            timestamp_id = self.generate_id()
            print(f"Step: {i} Timestamp ID: {timestamp_id}")
            sequence.append(timestamp_id)
        return sequence

    def validate_sequence(self, sequence: List[int]) -> bool:
        for i in range(1, len(sequence)):
            if sequence[i] <= sequence[i - 1]:
                print(f"Violation: {sequence[i - 1]} >= {sequence[i]}")
                return False
        return True


async def main():
    gen = TimestampGenerator()
    values = await gen.generate_sequence(1000)

    print("Generated values:", values)

    if gen.validate_sequence(values):
        print("All values are strictly increasing.")
    else:
        print("Sequence is not strictly increasing.")


if __name__ == "__main__":
    asyncio.run(main())
