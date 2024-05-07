from pathlib import Path
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-"


def text2speech(text):
    client = OpenAI()

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    # input=text
    input="我们正在讨论导航，也就是如何知道自己在哪里，以及如何前往想要去的其他地方。上次我们讨论了导航中的一般问题，谈到了海马旁区域以及其他涉及导航的大脑部分。今天我们将继续这个话题，但会更多地讨论实际参与这一过程的神经元群。我们将重点讨论导航中的一个具体方面，即重新定向。当你迷失方向时，就需要重新确定自己的位置，重新设置内部地图。随后我们将探讨整个导航系统的概念。尽管导航本身很有趣，但更令人兴奋的是，越来越多的证据表明我们可能会在高级认知中使用同一套系统。"
    )

    response.stream_to_file(speech_file_path)


text2speech("")